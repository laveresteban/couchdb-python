"""Server-level entry point for the hand-written CouchDB SDK."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import urllib3

import couchdb_client as gen

from .database import Database
from .errors import NotFound, translate


class CouchDB:
    """Connect to a CouchDB server.

    Reads (GET and HEAD) are retried up to `max_retries` times on 429, 502, 503
    and 504 and on connection errors, honoring `Retry-After`. Writes are never
    retried, since a retried write could apply twice.

    >>> with CouchDB("http://localhost:5984", "admin", "password") as couch:
    ...     db = couch.create_database("people")
    ...     db["alice"] = {"age": 30}
    """

    def __init__(self, url: str = "http://localhost:5984",
                 username: Optional[str] = None, password: Optional[str] = None,
                 max_retries: int = 3) -> None:
        # urllib3 accepts a Retry object here although the generated type says int.
        retry = urllib3.Retry(total=max_retries, backoff_factor=0.5,
                              status_forcelist=(429, 502, 503, 504),
                              allowed_methods=("GET", "HEAD"), raise_on_status=False)
        config = gen.Configuration(host=url.rstrip("/"), username=username, password=password,
                                   retries=retry)  # type: ignore[arg-type]
        self.client = gen.ApiClient(config)
        self._server = gen.ServerApi(self.client)
        self._auth = gen.AuthenticationApi(self.client)
        self._dbs = gen.DatabasesApi(self.client)
        self._replication = gen.ReplicationApi(self.client)

    def __enter__(self) -> "CouchDB":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def close(self) -> None:
        self.client.rest_client.pool_manager.clear()

    # -- server -----------------------------------------------------------
    def info(self) -> Dict[str, Any]:
        with translate():
            return self._server.get_server_information().to_dict()

    def up(self) -> bool:
        try:
            with translate():
                return self._server.get_up().status == "ok"
        except NotFound:
            return False

    def uuids(self, count: int = 1) -> List[str]:
        with translate():
            return self._server.get_uuids(count=count).uuids

    def all_dbs(self) -> List[str]:
        with translate():
            return self._server.get_all_dbs()

    def active_tasks(self) -> List[Dict[str, Any]]:
        """Running compactions, indexers and replications."""
        with translate():
            return [t.to_dict() for t in self._server.get_active_tasks()]

    def scheduler_jobs(self, limit: Optional[int] = None, skip: Optional[int] = None) -> Dict[str, Any]:
        """Replication jobs known to the scheduler."""
        with translate():
            return self._server.get_scheduler_jobs(limit=limit, skip=skip).to_dict()

    def scheduler_docs(self, limit: Optional[int] = None, skip: Optional[int] = None) -> Dict[str, Any]:
        """Replication documents known to the scheduler."""
        with translate():
            return self._server.get_scheduler_docs(limit=limit, skip=skip).to_dict()

    def node_config(self, node: str = "_local") -> Dict[str, Any]:
        """Configuration sections of one node, keyed by section name."""
        with translate():
            return self._server.get_node_config(node)

    # -- sessions ---------------------------------------------------------
    def login(self, name: str, password: str) -> None:
        """Start a cookie session; later requests send the AuthSession cookie."""
        with translate():
            res = self._auth.post_session_with_http_info(
                gen.SessionRequest(name=name, password=password))
        cookie = (res.headers or {}).get("Set-Cookie") or (res.headers or {}).get("set-cookie", "")
        self.client.cookie = cookie.split(";", 1)[0]

    def logout(self) -> None:
        with translate():
            self._auth.delete_session()
        self.client.cookie = None

    def session(self) -> Dict[str, Any]:
        with translate():
            info = self._auth.get_session()
        data = info.to_dict()
        data["userCtx"].setdefault("name", None)
        return data

    # -- databases --------------------------------------------------------
    def create_database(self, name: str, partitioned: bool = False) -> Database:
        with translate():
            self._dbs.put_database(name, partitioned=partitioned or None)
        return self[name]

    def delete_database(self, name: str) -> None:
        with translate():
            self._dbs.delete_database(name)

    def dbs_info(self, names: List[str]) -> List[Dict[str, Any]]:
        """Info for several databases in one request. Missing ones carry an `error`."""
        with translate():
            return [r.to_dict() for r in self._dbs.post_dbs_info(gen.DbsInfoRequest(keys=names))]

    def __getitem__(self, name: str) -> Database:
        return Database(self.client, name)

    def __contains__(self, name: object) -> bool:
        return self[str(name)].exists()

    # -- replication ------------------------------------------------------
    def _db_url(self, name: str) -> Dict[str, Any]:
        """Replication endpoint for a local database, carrying our credentials."""
        cfg = self.client.configuration
        endpoint: Dict[str, Any] = {"url": f"{cfg.host}/{name}"}
        if cfg.username:
            endpoint["auth"] = {"basic": {"username": cfg.username, "password": cfg.password}}
        return endpoint

    def replicate(self, source: str, target: str, **options: Any) -> Dict[str, Any]:
        """Replicate between databases. Bare names are resolved against this server."""
        def endpoint(x: str) -> Dict[str, Any]:
            return {"url": x} if "://" in x else self._db_url(x)

        body = {"source": endpoint(source), "target": endpoint(target), **options}
        with translate():
            return self._replication.post_replicate(gen.ReplicationRequest.from_dict(body)).to_dict()
