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
