"""Python implementation of the shared CouchDB SDK conformance steps.

The step text lives in couchdb-sdk-generator/conformance/specs and is the same
for every language; this file binds it to `couchdb_sdk`.
"""
import os
import uuid

from getgauge.python import after_scenario, data_store, step

from couchdb_sdk import CouchDB, CouchDBError, NotFound

URL = os.environ.get("COUCHDB_URL", "http://localhost:5984")
USER = os.environ.get("COUCHDB_USER", "admin")
PASSWORD = os.environ.get("COUCHDB_PASSWORD", "password")

s = data_store.scenario


def couch() -> CouchDB:
    return s["couch"]


def db():
    return s["db"]


def new_name() -> str:
    name = f"conformance_{uuid.uuid4().hex[:12]}"
    s.setdefault("cleanup", []).append(name)
    return name


def ints(csv):
    return [int(x) for x in csv.split(",") if x]


def assert_status(status, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except CouchDBError as err:
        assert err.status == int(status), f"expected {status}, got {err.status} ({err})"
        return
    raise AssertionError(f"expected HTTP {status}, but the call succeeded")


@after_scenario
def cleanup():
    if "couch" not in s:
        return
    with CouchDB(URL, USER, PASSWORD) as admin:
        for name in s.get("cleanup", []):
            if name in admin:
                admin.delete_database(name)
    couch().close()


# -- connections -----------------------------------------------------------
@step("Connect anonymously")
def connect_anonymously():
    s["couch"] = CouchDB(URL)


@step("Connect as admin")
def connect_as_admin():
    s["couch"] = CouchDB(URL, USER, PASSWORD)


# -- server ----------------------------------------------------------------
@step("Server information reports <welcome>")
def server_info_reports(welcome):
    assert couch().info()["couchdb"] == welcome


@step("Server is up")
def server_is_up():
    assert couch().up()


@step("Request <count> UUIDs and receive <unique> unique values")
def request_uuids(count, unique):
    assert len(set(couch().uuids(int(count)))) == int(unique)


# -- authentication --------------------------------------------------------
@step("Log in with the admin credentials")
def log_in():
    couch().login(USER, PASSWORD)


@step("The session user is the admin user")
def session_is_admin():
    assert couch().session()["userCtx"]["name"] == USER


@step("Log out")
def log_out():
    couch().logout()


@step("The session user is anonymous")
def session_is_anonymous():
    assert couch().session()["userCtx"]["name"] is None


@step("Logging in with password <password> fails with status <status>")
def login_fails(password, status):
    assert_status(status, couch().login, USER, password)


# -- databases -------------------------------------------------------------
@step("Create a fresh database")
def create_database():
    s["db"] = couch().create_database(new_name())


@step("Create a fresh partitioned database")
def create_partitioned_database():
    s["db"] = couch().create_database(new_name(), partitioned=True)


@step("The database exists")
def database_exists():
    assert db().exists()


@step("The database does not exist")
def database_does_not_exist():
    assert not db().exists()


@step("The database is listed among all databases")
def database_listed():
    assert db().name in couch().all_dbs()


@step("The database has <count> documents")
def database_doc_count(count):
    assert db().info()["doc_count"] == int(count)


@step("Delete the database")
def delete_database():
    couch().delete_database(db().name)


@step("Creating the same database again fails with status <status>")
def create_again_fails(status):
    assert_status(status, couch().create_database, db().name)


# -- documents -------------------------------------------------------------
@step("Save document <docid> with field <field> = <value>")
def save_document(docid, field, value):
    db().save({"_id": docid, field: value})


@step("Document <docid> has field <field> = <value>")
def document_has_field(docid, field, value):
    assert db()[docid][field] == value


@step("Update document <docid> setting field <field> = <value>")
def update_document(docid, field, value):
    db().update(docid, lambda d: {**d, field: value})


@step("Document <docid> has a revision starting with <prefix>")
def revision_prefix(docid, prefix):
    assert db()[docid]["_rev"].startswith(prefix)


@step("Delete document <docid>")
def delete_document(docid):
    del db()[docid]


@step("Document <docid> does not exist")
def document_missing(docid):
    assert docid not in db()


@step("Remember the revision of document <docid>")
def remember_revision(docid):
    s["rev"] = db()[docid]["_rev"]


@step("Saving document <docid> with the remembered revision fails with status <status>")
def stale_save_fails(docid, status):
    assert_status(status, db().save, {"_id": docid, "_rev": s["rev"]})


@step("Create a document without an id with field <field> = <value>")
def create_without_id(field, value):
    s["created"] = db().save({field: value})["_id"]


@step("The created document can be read back with field <field> = <value>")
def read_created(field, value):
    assert db()[s["created"]][field] == value


@step("Bulk save <count> documents with field <field> = <value>")
def bulk_save(count, field, value):
    results = db().bulk_save([{field: value} for _ in range(int(count))])
    assert all(r.get("ok") for r in results), results


@step("All documents lists <count> rows")
def all_docs_rows(count):
    assert len(db().all_docs()) == int(count)


# -- Mango queries ---------------------------------------------------------
@step("Bulk save documents with ages <ages>")
def bulk_save_ages(ages):
    db().bulk_save([{"age": a} for a in ints(ages)])


@step("Finding documents with age greater than <age> returns ages <ages>")
def find_ages(age, ages):
    res = db().find({"age": {"$gt": int(age)}})
    assert sorted(d["age"] for d in res.docs) == sorted(ints(ages))


@step("Create a json index on field <field> named <name>")
def create_index(field, name):
    db().create_index([field], name=name)


@step("The index <name> is listed")
def index_listed(name):
    assert name in [i["name"] for i in db().indexes()]


@step("Finding documents with age greater than <age> sorted descending returns ages <ages>")
def find_sorted(age, ages):
    res = db().find({"age": {"$gt": int(age)}}, sort=[{"age": "desc"}])
    assert [d["age"] for d in res.docs] == ints(ages)


@step("Finding documents with age greater than <age> with limit <limit> returns <count> documents and a bookmark")
def find_page(age, limit, count):
    s["page_query"] = ({"age": {"$gt": int(age)}}, int(limit))
    res = db().find(s["page_query"][0], limit=int(limit))
    assert len(res.docs) == int(count) and res.bookmark
    s["bookmark"], s["seen"] = res.bookmark, {d["_id"] for d in res.docs}


@step("Continuing from the bookmark returns <count> more documents")
def find_next_page(count):
    selector, limit = s["page_query"]
    res = db().find(selector, limit=limit, bookmark=s["bookmark"])
    ids = {d["_id"] for d in res.docs}
    assert len(ids) == int(count) and not ids & s["seen"]


# -- design documents and views --------------------------------------------
@step("Save design document <ddoc> with view <view> emitting age and reducing with <reduce>")
def save_design(ddoc, view, reduce):
    db().save_design(ddoc, {view: {"map": "function (doc) { emit(doc.age, doc.age); }", "reduce": reduce}})


@step("Design document <ddoc> has view <view>")
def design_has_view(ddoc, view):
    assert view in db().design(ddoc)["views"]


def split_view(path):
    ddoc, view = path.split("/")
    return ddoc, view


@step("Querying view <path> without reduce returns <count> rows")
def view_rows(path, count):
    assert len(db().view(*split_view(path), reduce=False)) == int(count)


@step("Querying view <path> with reduce returns the value <value>")
def view_reduce(path, value):
    rows = db().view(*split_view(path), reduce=True)
    assert rows[0]["value"] == int(value), rows


@step("Delete design document <ddoc>")
def delete_design(ddoc):
    db().delete_design(ddoc)


@step("Design document <ddoc> does not exist")
def design_missing(ddoc):
    try:
        db().design(ddoc)
    except NotFound:
        return
    raise AssertionError(f"design document {ddoc} still exists")


# -- attachments -----------------------------------------------------------
@step("Attach <data> as <name> to document <docid>")
def attach(data, name, docid):
    db().put_attachment(docid, name, data.encode(), "text/plain")


@step("Attachment <name> of document <docid> contains <data>")
def attachment_contains(name, docid, data):
    assert db().get_attachment(docid, name) == data.encode()


@step("Document <docid> lists attachment <name>")
def document_lists_attachment(docid, name):
    assert name in db()[docid].get("_attachments", {})


@step("Delete attachment <name> from document <docid>")
def delete_attachment(name, docid):
    db().delete_attachment(docid, name)


@step("Attachment <name> of document <docid> does not exist")
def attachment_missing(name, docid):
    try:
        db().get_attachment(docid, name)
    except NotFound:
        return
    raise AssertionError(f"attachment {name} still exists")


# -- changes ---------------------------------------------------------------
@step("The changes feed lists documents <ids>")
def changes_list(ids):
    assert sorted(r["id"] for r in db().changes().results) == sorted(ids.split(","))


@step("Remember the current update sequence")
def remember_seq():
    s["seq"] = db().changes().last_seq


@step("The changes feed since the remembered sequence lists documents <ids>")
def changes_since(ids):
    got = [r["id"] for r in db().changes(since=s["seq"]).results]
    assert sorted(got) == sorted(ids.split(",")), got


@step("The changes feed marks document <docid> as deleted")
def changes_deleted(docid):
    rows = [r for r in db().changes().results if r["id"] == docid]
    assert rows and rows[-1].get("deleted") is True, rows


@step("The changes feed filtered to documents <ids> lists documents <expected>")
def changes_doc_ids(ids, expected):
    got = [r["id"] for r in db().changes(doc_ids=ids.split(",")).results]
    assert sorted(got) == sorted(expected.split(",")), got


@step("Follow the changes feed with checkpoint <name> until document <docid>")
def follow_until(name, docid):
    feed = db().follow(checkpoint=name, timeout=1000)
    for row in feed:
        if row["id"] == docid:
            feed.stop()


@step("Following the changes feed with checkpoint <name> next yields document <docid>")
def follow_next(name, docid):
    row = next(iter(db().follow(checkpoint=name, timeout=1000)))
    assert row["id"] == docid, row


@step("Follow the continuous changes feed with checkpoint <name> until document <docid>")
def follow_continuous_until(name, docid):
    feed = db().follow(feed="continuous", checkpoint=name, heartbeat=1000, batch_size=1)
    for row in feed:
        if row["id"] == docid:
            feed.stop()


@step("Following the continuous changes feed with checkpoint <name> next yields document <docid>")
def follow_continuous_next(name, docid):
    row = next(iter(db().follow(feed="continuous", checkpoint=name, heartbeat=1000)))
    assert row["id"] == docid, row


# -- security --------------------------------------------------------------
@step("Set the database members to user <user>")
def set_members(user):
    db().set_security(members={"names": [user], "roles": []})


@step("The database members include user <user>")
def members_include(user):
    assert user in db().security()["members"]["names"]


@step("Anonymous access to the database fails with status <status>")
def anonymous_denied(status):
    with CouchDB(URL) as anon:
        assert_status(status, anon[db().name].info)


# -- partitions ------------------------------------------------------------
@step("All documents in partition <partition> lists <count> rows")
def partition_all_docs(partition, count):
    assert len(db().partition(partition).all_docs()) == int(count)


@step("Finding in partition <partition> for field <field> = <value> returns <count> documents")
def partition_find(partition, field, value, count):
    assert len(db().partition(partition).find({field: value}).docs) == int(count)


# -- replication -----------------------------------------------------------
@step("Replicate the database to a new database")
def replicate():
    s["replica"] = new_name()
    couch().replicate(db().name, s["replica"], create_target=True)


@step("The replica has <count> documents")
def replica_count(count):
    assert couch()[s["replica"]].info()["doc_count"] == int(count)


# -- sync primitives -------------------------------------------------------
@step("Revs diff for document <docid> with the remembered revision reports nothing missing")
def revs_diff_nothing_missing(docid):
    assert db().revs_diff({docid: [s["rev"]]}) == {}


@step("Revs diff for document <docid> with revision <rev> reports <missing> missing")
def revs_diff_missing(docid, rev, missing):
    assert db().revs_diff({docid: [rev]})[docid]["missing"] == missing.split(",")


@step("Bulk get documents <ids> with history returns <count> documents")
def bulk_get_docs(ids, count):
    res = db().bulk_get([{"id": i} for i in ids.split(",")], revs=True)
    docs = [d["ok"] for r in res for d in r["docs"] if "ok" in d]
    assert len(docs) == int(count), res
    assert all("_revisions" in d for d in docs), docs


@step("Bulk get history of document <docid> lists <count> revisions")
def bulk_get_history(docid, count):
    doc = db().bulk_get([{"id": docid}], revs=True)[0]["docs"][0]["ok"]
    assert len(doc["_revisions"]["ids"]) == int(count), doc


@step("Bulk get of missing document <docid> reports <error>")
def bulk_get_missing(docid, error):
    entry = db().bulk_get([{"id": docid}])[0]["docs"][0]
    assert entry.get("error", {}).get("error") == error, entry


@step("Save local document <docid> with field <field> = <value>")
def save_local(docid, field, value):
    db().put_local(docid, {field: value})


@step("Local document <docid> has field <field> = <value>")
def local_has_field(docid, field, value):
    assert db().get_local(docid)[field] == value


@step("The changes feed lists no documents")
def changes_empty():
    assert db().changes().results == []


@step("Delete local document <docid>")
def delete_local(docid):
    db().delete_local(docid)


@step("Local document <docid> does not exist")
def local_missing(docid):
    try:
        db().get_local(docid)
    except NotFound:
        return
    raise AssertionError(f"_local/{docid} still exists")


@step("Write document <docid> at revision <rev> with field <field> = <value> without new edits")
def write_without_new_edits(docid, rev, field, value):
    db().bulk_save([{"_id": docid, "_rev": rev, field: value}], new_edits=False)


@step("Document <docid> has <count> conflicts")
def conflict_count(docid, count):
    assert len(db().get(docid, conflicts=True).get("_conflicts", [])) == int(count)


@step("The changes feed with all leaf revisions lists <count> revisions for document <docid>")
def changes_all_leaves(count, docid):
    rows = [r for r in db().changes(style="all_docs").results if r["id"] == docid]
    assert rows and len(rows[-1]["changes"]) == int(count), rows


@step("Document <docid> with revision history lists <count> revisions")
def revision_history(docid, count):
    assert len(db().get(docid, revs=True)["_revisions"]["ids"]) == int(count)


@step("The changes feed filtered by field <field> = <value> lists documents <ids>")
def changes_by_selector(field, value, ids):
    got = [r["id"] for r in db().changes(selector={field: value}).results]
    assert sorted(got) == sorted(ids.split(",")), got
