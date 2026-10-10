"""Pythonic database handle over the generated couchdb_client APIs."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

import couchdb_client as gen

from .changes import ChangesFeed
from .errors import Conflict, NotFound, translate

Doc = Dict[str, Any]


@dataclass
class FindResult:
    docs: List[Doc]
    bookmark: Optional[str] = None
    warning: Optional[str] = None


@dataclass
class ChangesResult:
    results: List[Dict[str, Any]]
    last_seq: str
    pending: Optional[int] = None


def _plain(model: Any) -> Any:
    return model.to_dict() if hasattr(model, "to_dict") else model


def _rows(result: Any) -> List[Dict[str, Any]]:
    return [_plain(r) for r in (result.rows or [])]


def _find_result(res: Any) -> FindResult:
    return FindResult([_plain(d) for d in res.docs], res.bookmark, res.warning)


# Models are built with their constructors, not from_dict: from_dict marks every
# field as set, so untyped fields like start_key would be sent as null.
def _find_query(selector: Doc, kwargs: Dict[str, Any]) -> Any:
    return gen.FindQuery(selector=selector, **kwargs)


@dataclass
class Partition:
    database: "Database"
    name: str

    def all_docs(self, **kwargs: Any) -> List[Dict[str, Any]]:
        with translate():
            res = self.database._partitions.post_partition_all_docs(
                self.database.name, self.name, gen.AllDocsQuery(**kwargs))
        return _rows(res)

    def find(self, selector: Doc, **kwargs: Any) -> FindResult:
        with translate():
            res = self.database._partitions.post_partition_find(
                self.database.name, self.name, _find_query(selector, kwargs))
        return _find_result(res)


@dataclass
class Database:
    """A CouchDB database. Documents are plain dicts; `save` keeps `_rev` current."""

    client: Any = field(repr=False)
    name: str

    def __post_init__(self) -> None:
        c = self.client
        self._dbs = gen.DatabasesApi(c)
        self._docs = gen.DocumentsApi(c)
        self._query = gen.QueryApi(c)
        self._design = gen.DesignDocumentsApi(c)
        self._attachments = gen.AttachmentsApi(c)
        self._changes = gen.ChangesApi(c)
        self._security = gen.SecurityApi(c)
        self._partitions = gen.PartitionsApi(c)
        self._replication = gen.ReplicationApi(c)

    # -- database ---------------------------------------------------------
    def info(self) -> Dict[str, Any]:
        with translate():
            return _plain(self._dbs.get_database_information(self.name))

    def exists(self) -> bool:
        try:
            self.info()
            return True
        except NotFound:
            return False

    # -- documents --------------------------------------------------------
    def get(self, docid: str, **kwargs: Any) -> Doc:
        with translate():
            return _plain(self._docs.get_document(self.name, docid, **kwargs))

    def save(self, doc: Doc) -> Doc:
        """Create or update `doc` in place, setting its `_id` and `_rev`."""
        body = gen.Document.from_dict(doc)
        with translate():
            if "_id" in doc:
                res = self._docs.put_document(self.name, doc["_id"], body)
            else:
                res = self._docs.post_document(self.name, body)
        doc["_id"], doc["_rev"] = res.id, res.rev
        return doc

    def delete(self, doc_or_id: Any) -> None:
        doc = self.get(doc_or_id) if isinstance(doc_or_id, str) else doc_or_id
        with translate():
            self._docs.delete_document(self.name, doc["_id"], rev=doc["_rev"])

    def update(self, docid: str, fn: Callable[[Doc], Doc], retries: int = 5) -> Doc:
        """Apply `fn` to the latest revision, retrying on conflicts."""
        for attempt in range(retries):
            try:
                return self.save(fn(self.get(docid)))
            except Conflict:
                if attempt == retries - 1:
                    raise
        raise AssertionError("unreachable")

    def bulk_save(self, docs: List[Doc], new_edits: bool = True) -> List[Dict[str, Any]]:
        """Write many docs at once. Docs that were saved get their new `_id`/`_rev`.

        With `new_edits=False` the docs keep the `_rev` (and `_revisions`) you
        give them, the way a replicator writes; CouchDB then only reports failures.
        """
        body: Dict[str, Any] = {"docs": docs}
        if not new_edits:
            body["new_edits"] = False
        with translate():
            res = [_plain(r) for r in self._docs.post_bulk_docs(self.name, gen.BulkDocs.from_dict(body))]
        if new_edits:
            for doc, row in zip(docs, res):
                if row.get("ok") or (row.get("rev") and not row.get("error")):
                    doc["_id"], doc["_rev"] = row["id"], row["rev"]
        return res

    def __getitem__(self, docid: str) -> Doc:
        return self.get(docid)

    def __setitem__(self, docid: str, doc: Doc) -> None:
        doc = dict(doc, _id=docid)
        if "_rev" not in doc:
            try:
                doc["_rev"] = self.get(docid)["_rev"]
            except NotFound:
                pass
        self.save(doc)

    def __delitem__(self, docid: str) -> None:
        self.delete(docid)

    def __contains__(self, docid: object) -> bool:
        try:
            self.get(str(docid))
            return True
        except NotFound:
            return False

    # -- queries ----------------------------------------------------------
    def all_docs(self, **kwargs: Any) -> List[Dict[str, Any]]:
        with translate():
            return _rows(self._query.post_all_docs(self.name, gen.AllDocsQuery(**kwargs)))

    def find(self, selector: Doc, **kwargs: Any) -> FindResult:
        with translate():
            return _find_result(self._query.post_find(self.name, _find_query(selector, kwargs)))

    def create_index(self, fields: List[str], name: Optional[str] = None, **kwargs: Any) -> Dict[str, Any]:
        body = {"index": {"fields": fields}, **kwargs}
        if name:
            body["name"] = name
        with translate():
            return _plain(self._query.post_index(self.name, gen.IndexDefinitionRequest.from_dict(body)))

    def indexes(self) -> List[Dict[str, Any]]:
        with translate():
            return [_plain(i) for i in self._query.get_indexes(self.name).indexes]

    # -- design documents and views ---------------------------------------
    def design(self, name: str) -> Doc:
        with translate():
            return _plain(self._design.get_design_document(self.name, name))

    def save_design(self, name: str, views: Dict[str, Dict[str, str]], **extra: Any) -> Doc:
        doc: Doc = {"_id": f"_design/{name}", "views": views, **extra}
        try:
            doc["_rev"] = self.design(name)["_rev"]
        except NotFound:
            pass
        with translate():
            res = self._design.put_design_document(self.name, name, gen.DesignDocument.from_dict(doc))
        doc["_rev"] = res.rev
        return doc

    def delete_design(self, name: str) -> None:
        rev = self.design(name)["_rev"]
        with translate():
            self._design.delete_design_document(self.name, name, rev=rev)

    def view(self, ddoc: str, view: str, **kwargs: Any) -> List[Dict[str, Any]]:
        with translate():
            return _rows(self._design.post_view(self.name, ddoc, view, gen.ViewQuery(**kwargs)))

    # -- attachments ------------------------------------------------------
    def put_attachment(self, docid: str, name: str, data: bytes,
                       content_type: str = "application/octet-stream") -> str:
        """Attach `data` to `docid` (creating the doc if needed); returns the new rev."""
        try:
            rev: Optional[str] = self.get(docid)["_rev"]
        except NotFound:
            rev = None
        with translate():
            res = self._attachments.put_attachment(
                self.name, docid, name, data, rev=rev, _content_type=content_type)
        return res.rev

    def get_attachment(self, docid: str, name: str) -> bytes:
        with translate():
            return bytes(self._attachments.get_attachment(self.name, docid, name))

    def delete_attachment(self, docid: str, name: str) -> str:
        rev = self.get(docid)["_rev"]
        with translate():
            return self._attachments.delete_attachment(self.name, docid, name, rev=rev).rev

    # -- changes ----------------------------------------------------------
    def changes(self, since: str = "0", doc_ids: Optional[List[str]] = None,
                selector: Optional[Doc] = None, **kwargs: Any) -> ChangesResult:
        """One page of changes. `doc_ids` or `selector` filter server-side."""
        with translate():
            if doc_ids is None and selector is None:
                res = self._changes.get_changes(self.name, since=since, **kwargs)
            else:
                kwargs.setdefault("filter", "_selector" if selector is not None else "_doc_ids")
                body = gen.ChangesQuery(doc_ids=doc_ids, selector=selector)
                res = self._changes.post_changes(self.name, body, since=since, **kwargs)
        return ChangesResult([_plain(r) for r in res.results], res.last_seq, res.pending)

    def follow(self, **kwargs: Any) -> ChangesFeed:
        """Iterate changes forever; see `ChangesFeed` for retry and checkpoint options."""
        return ChangesFeed(self, **kwargs)

    # -- replication primitives -------------------------------------------
    def revs_diff(self, revs: Dict[str, List[str]]) -> Dict[str, Dict[str, Any]]:
        """Which of the given revisions this database is missing, per doc id."""
        with translate():
            res = self._replication.post_revs_diff(self.name, revs)
        return {docid: _plain(v) for docid, v in res.items()}

    def bulk_get(self, docs: List[Dict[str, Any]], revs: bool = False, latest: bool = False,
                 attachments: bool = False) -> List[Dict[str, Any]]:
        """Fetch many docs/revisions at once. `docs` items are `{"id", "rev"?, "atts_since"?}`.

        Returns one entry per requested id: `{"id": ..., "docs": [{"ok": doc} | {"error": {...}}]}`.
        """
        with translate():
            res = self._replication.post_bulk_get(
                self.name, gen.BulkGetRequest.from_dict({"docs": docs}),
                revs=revs or None, latest=latest or None, attachments=attachments or None)
        return [_plain(r) for r in res.results]

    # -- local documents --------------------------------------------------
    def get_local(self, docid: str) -> Doc:
        with translate():
            return _plain(self._docs.get_local_document(self.name, docid))

    def put_local(self, docid: str, doc: Doc) -> Doc:
        """Write `_local/<docid>` (not replicated, not in the changes feed)."""
        with translate():
            res = self._docs.put_local_document(self.name, docid, gen.Document.from_dict(doc))
        return dict(doc, _id=res.id, _rev=res.rev)

    def delete_local(self, docid: str, rev: Optional[str] = None) -> None:
        if rev is None:
            rev = self.get_local(docid).get("_rev")
        with translate():
            self._docs.delete_local_document(self.name, docid, rev=rev)

    # -- security ---------------------------------------------------------
    def security(self) -> Dict[str, Any]:
        with translate():
            return _plain(self._security.get_security(self.name))

    def set_security(self, admins: Optional[Doc] = None, members: Optional[Doc] = None) -> None:
        body = {"admins": admins or {"names": [], "roles": []},
                "members": members or {"names": [], "roles": []}}
        with translate():
            self._security.put_security(self.name, gen.Security.from_dict(body))

    # -- partitions -------------------------------------------------------
    def partition(self, name: str) -> Partition:
        return Partition(self, name)
