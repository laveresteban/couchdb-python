import couchdb_client
from couchdb_client.exceptions import NotFoundException


def test_server_information(api_client):
    info = couchdb_client.ServerApi(api_client).get_server_information()
    assert info.couchdb == "Welcome"


def test_database_lifecycle(api_client, db):
    dbs = couchdb_client.DatabasesApi(api_client)
    assert db in couchdb_client.ServerApi(api_client).get_all_dbs()
    assert dbs.get_database_information(db).db_name == db


def test_document_crud(api_client, db):
    docs = couchdb_client.DocumentsApi(api_client)
    created = docs.put_document(db, "doc1", couchdb_client.Document.from_dict({"name": "alice"}))
    assert created.ok

    fetched = docs.get_document(db, "doc1")
    assert fetched.to_dict()["name"] == "alice"

    docs.delete_document(db, "doc1", rev=created.rev)
    try:
        docs.get_document(db, "doc1")
        raise AssertionError("expected 404")
    except NotFoundException:
        pass


def test_bulk_docs_and_find(api_client, db):
    docs = couchdb_client.DocumentsApi(api_client)
    docs.post_bulk_docs(db, couchdb_client.BulkDocs.from_dict(
        {"docs": [{"type": "user", "age": a} for a in (20, 30, 40)]}
    ))
    query = couchdb_client.QueryApi(api_client)
    result = query.post_find(db, couchdb_client.FindQuery.from_dict(
        {"selector": {"age": {"$gt": 25}}}
    ))
    assert sorted(d.to_dict()["age"] for d in result.docs) == [30, 40]
