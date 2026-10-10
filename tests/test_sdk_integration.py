"""Integration tests for the hand-written couchdb_sdk layer against a real CouchDB."""
import threading
import time

import pytest

from couchdb_sdk import CouchDB, errors
from tests.conftest import PASSWORD, URL, USER, unique_name


def test_server(couch):
    assert couch.info()["couchdb"] == "Welcome"
    assert couch.up()
    assert len(set(couch.uuids(3))) == 3


def test_database_lifecycle(couch):
    name = unique_name()
    couch.create_database(name)
    assert name in couch
    assert name in couch.all_dbs()
    with pytest.raises(errors.PreconditionFailed):
        couch.create_database(name)
    couch.delete_database(name)
    assert name not in couch


def test_dict_like_documents(database):
    database["doc1"] = {"name": "alice"}
    assert database["doc1"]["name"] == "alice"
    assert "doc1" in database
    del database["doc1"]
    assert "doc1" not in database
    with pytest.raises(KeyError):
        database["doc1"]


def test_save_tracks_revisions(database):
    doc = database.save({"_id": "a", "n": 1})
    assert doc["_rev"].startswith("1-")
    doc["n"] = 2
    database.save(doc)
    assert doc["_rev"].startswith("2-")


def test_save_without_id_gets_server_id(database):
    doc = database.save({"kind": "auto"})
    assert database[doc["_id"]]["kind"] == "auto"


def test_stale_revision_conflicts(database):
    first = database.save({"_id": "a"})
    stale = dict(first)
    database.save(first)
    with pytest.raises(errors.Conflict):
        database.save(stale)


def test_update_with_function(database):
    database.save({"_id": "counter", "n": 0})
    assert database.update("counter", lambda d: {**d, "n": d["n"] + 1})["n"] == 1


def test_bulk_all_docs_and_find(database):
    results = database.bulk_save([{"age": a} for a in (20, 30, 40)])
    assert all(r["ok"] for r in results)
    assert len(database.all_docs()) == 3
    assert database.info()["doc_count"] == 3
    database.create_index(["age"], name="age-idx")
    assert "age-idx" in [i["name"] for i in database.indexes()]
    res = database.find({"age": {"$gt": 25}}, sort=[{"age": "desc"}])
    assert [d["age"] for d in res.docs] == [40, 30]


def test_views(database):
    database.bulk_save([{"age": a} for a in (1, 2, 3)])
    database.save_design("stats", {"by_age": {"map": "function(d){ emit(d.age, d.age); }", "reduce": "_sum"}})
    assert "by_age" in database.design("stats")["views"]
    assert len(database.view("stats", "by_age", reduce=False)) == 3
    assert database.view("stats", "by_age")[0]["value"] == 6
    database.delete_design("stats")
    with pytest.raises(errors.NotFound):
        database.design("stats")


def test_attachments(database):
    database.save({"_id": "f"})
    database.put_attachment("f", "a.txt", b"hello", "text/plain")
    assert database.get_attachment("f", "a.txt") == b"hello"
    assert "a.txt" in database["f"]["_attachments"]
    database.delete_attachment("f", "a.txt")
    with pytest.raises(errors.NotFound):
        database.get_attachment("f", "a.txt")


def test_changes(database):
    database.save({"_id": "a"})
    first = database.changes()
    assert [r["id"] for r in first.results] == ["a"]
    database.save({"_id": "b"})
    assert [r["id"] for r in database.changes(since=first.last_seq).results] == ["b"]


def test_security(couch, database):
    database.set_security(members={"names": ["alice"], "roles": []})
    assert database.security()["members"]["names"] == ["alice"]
    with CouchDB(URL) as anon:
        with pytest.raises(errors.Unauthorized):
            anon[database.name].info()


def test_partitions(couch):
    name = unique_name()
    d = couch.create_database(name, partitioned=True)
    try:
        d.bulk_save([{"_id": "red:1"}, {"_id": "red:2"}, {"_id": "blue:1", "c": "blue"}])
        assert len(d.partition("red").all_docs()) == 2
        assert len(d.partition("blue").find({"c": "blue"}).docs) == 1
    finally:
        couch.delete_database(name)


def test_replicate(couch, database):
    database.bulk_save([{"i": i} for i in range(5)])
    target = unique_name()
    try:
        couch.replicate(database.name, target, create_target=True)
        assert couch[target].info()["doc_count"] == 5
    finally:
        couch.delete_database(target)


def test_cookie_session():
    with CouchDB(URL) as c:
        c.login(USER, PASSWORD)
        assert c.session()["userCtx"]["name"] == USER
        c.logout()
        assert c.session()["userCtx"]["name"] is None


def test_changes_filters(database):
    database.bulk_save([{"_id": "a", "t": 1}, {"_id": "b", "t": 2}, {"_id": "c", "t": 1}])
    assert [r["id"] for r in database.changes(doc_ids=["b"]).results] == ["b"]
    assert sorted(r["id"] for r in database.changes(selector={"t": 1}).results) == ["a", "c"]


def test_follow_resumes_from_checkpoint(database):
    database.bulk_save([{"_id": "a"}, {"_id": "b"}])
    feed = database.follow(checkpoint="reader", timeout=1000)
    seen = []
    for row in feed:
        seen.append(row["id"])
        if len(seen) == 2:
            feed.stop()
    assert sorted(seen) == ["a", "b"]

    database.save({"_id": "c"})
    feed = database.follow(checkpoint="reader", timeout=1000)
    assert next(iter(feed))["id"] == "c"


def test_follow_continuous_delivers_live_writes(database):
    database.save({"_id": "a"})
    feed = database.follow(feed="continuous", heartbeat=1000)

    def write_later():
        time.sleep(0.5)
        database.save({"_id": "b"})

    writer = threading.Thread(target=write_later)
    writer.start()
    seen = []
    try:
        for row in feed:
            seen.append(row["id"])
            if "b" in seen:
                feed.stop()
    finally:
        writer.join()
    assert set(seen) >= {"a", "b"}


def test_follow_continuous_resumes_from_checkpoint(database):
    database.bulk_save([{"_id": "a"}, {"_id": "b"}])
    feed = database.follow(feed="continuous", checkpoint="cont", heartbeat=1000, batch_size=1)
    seen = []
    for row in feed:
        seen.append(row["id"])
        if len(seen) == 2:
            feed.stop()
    assert sorted(seen) == ["a", "b"]

    database.save({"_id": "c"})
    feed = database.follow(feed="continuous", checkpoint="cont", heartbeat=1000)
    assert next(iter(feed))["id"] == "c"
