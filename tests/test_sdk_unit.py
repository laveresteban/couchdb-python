"""Unit tests for couchdb_sdk logic that does not need a server."""
from unittest import mock

import pytest

from couchdb_client.exceptions import ApiException
from couchdb_sdk import errors
from couchdb_sdk.database import Database


def api_error(status, error="x", reason="y"):
    exc = ApiException(status=status, reason=reason)
    exc.body = f'{{"error": "{error}", "reason": "{reason}"}}'
    return exc


@pytest.mark.parametrize("status,cls", [
    (401, errors.Unauthorized),
    (403, errors.Forbidden),
    (404, errors.NotFound),
    (409, errors.Conflict),
    (412, errors.PreconditionFailed),
    (500, errors.CouchDBError),
])
def test_api_exceptions_map_to_typed_errors(status, cls):
    err = errors.from_api_exception(api_error(status, "e", "why"))
    assert type(err) is cls
    assert (err.status, err.error, err.reason) == (status, "e", "why")


def test_error_body_that_is_not_json_is_kept_as_reason():
    exc = ApiException(status=500, reason="Internal")
    exc.body = "<html>oops</html>"
    err = errors.from_api_exception(exc)
    assert err.status == 500 and "oops" in err.reason


def test_not_found_is_a_key_error():
    assert issubclass(errors.NotFound, KeyError)


def test_translate_reraises_typed_error():
    with pytest.raises(errors.Conflict):
        with errors.translate():
            raise api_error(409, "conflict", "Document update conflict.")


def make_db():
    return Database(client=mock.MagicMock(), name="db")


def test_update_retries_on_conflict_then_succeeds():
    d = make_db()
    docs = [{"_id": "a", "_rev": "1-x", "n": 1}, {"_id": "a", "_rev": "2-y", "n": 5}]
    saved = {"_id": "a", "_rev": "3-z", "n": 6}
    with mock.patch.object(d, "get", side_effect=[dict(x) for x in docs]), \
         mock.patch.object(d, "save", side_effect=[errors.Conflict(409, "conflict", ""), saved]) as save:
        result = d.update("a", lambda doc: {**doc, "n": doc["n"] + 1})
    assert result["n"] == 6
    assert save.call_count == 2
    assert save.call_args_list[1].args[0]["n"] == 6


def test_update_gives_up_after_retries():
    d = make_db()
    with mock.patch.object(d, "get", return_value={"_id": "a", "_rev": "1-x"}), \
         mock.patch.object(d, "save", side_effect=errors.Conflict(409, "conflict", "")) as save:
        with pytest.raises(errors.Conflict):
            d.update("a", lambda doc: doc, retries=3)
    assert save.call_count == 3


def test_changes_feed_retries_transient_errors_then_raises_fatal():
    from couchdb_sdk.changes import ChangesFeed
    from couchdb_sdk.database import ChangesResult

    db = mock.Mock()
    db.changes.side_effect = [
        errors.CouchDBError(503, "e", "r"),
        ChangesResult([{"id": "a", "seq": "1"}], "1"),
        errors.NotFound(404, "not_found", "Database does not exist."),
    ]
    feed = ChangesFeed(db)
    rows = []
    with mock.patch("couchdb_sdk.changes.time.sleep") as sleep, pytest.raises(errors.NotFound):
        for row in feed:
            rows.append(row)
    assert rows == [{"id": "a", "seq": "1"}]
    assert feed.since == "1"
    assert 0.5 <= sleep.call_args[0][0] <= 1.0


def test_changes_feed_gives_up_after_max_retries():
    from couchdb_sdk.changes import ChangesFeed

    db = mock.Mock()
    db.changes.side_effect = errors.CouchDBError(500, "e", "r")
    with mock.patch("couchdb_sdk.changes.time.sleep"), pytest.raises(errors.CouchDBError):
        list(ChangesFeed(db, max_retries=2))
    assert db.changes.call_count == 3


def test_changes_feed_honors_retry_after():
    from couchdb_sdk.changes import ChangesFeed

    busy = errors.CouchDBError(429, "e", "r")
    busy.headers = {"Retry-After": "7"}
    db = mock.Mock()
    db.changes.side_effect = [busy, errors.NotFound(404, "x", "y")]
    with mock.patch("couchdb_sdk.changes.time.sleep") as sleep, pytest.raises(errors.NotFound):
        list(ChangesFeed(db))
    sleep.assert_called_once_with(7.0)


def test_api_exception_headers_are_kept():
    exc = api_error(503)
    exc.headers = {"Retry-After": "3"}
    assert errors.from_api_exception(exc).headers["Retry-After"] == "3"


# -- continuous changes feed ------------------------------------------------

class FakeStream:
    """A urllib3-like streaming response. Items that are exceptions are raised
    mid-stream to simulate a dropped connection."""

    def __init__(self, chunks, status=200, body=b""):
        self.status = status
        self._chunks = list(chunks)
        self._body = body
        self.headers = {}

    def stream(self, amt=None, decode_content=True):
        for chunk in self._chunks:
            if isinstance(chunk, Exception):
                raise chunk
            yield chunk

    def read(self):
        return self._body

    def release_conn(self):
        pass


def continuous_feed(opens, **kwargs):
    """A ChangesFeed whose _open() returns each FakeStream in turn."""
    from couchdb_sdk.changes import ChangesFeed

    db = mock.Mock()
    db.name = "db"
    feed = ChangesFeed(db, feed="continuous", **kwargs)
    feed._open = mock.Mock(side_effect=list(opens))
    return feed


def test_continuous_yields_changes_and_skips_heartbeats():
    # A JSON change, a heartbeat (blank line), another change, then last_seq.
    stream = FakeStream([
        b'{"seq":"1","id":"a","changes":[]}\n',
        b"\n",  # heartbeat
        b'{"seq":"2","id":"b","changes":[]}\n{"last_seq":"2","pending":0}\n',
    ])
    feed = continuous_feed([stream])
    feed._stopped = False
    rows = []
    for row in feed:
        rows.append(row)
        if len(rows) == 2:
            feed.stop()
    assert [r["id"] for r in rows] == ["a", "b"]
    assert feed.since == "2"


def test_continuous_reconnects_from_last_seq_on_transient_drop():
    import urllib3

    dropped = FakeStream([
        b'{"seq":"1","id":"a","changes":[]}\n',
        urllib3.exceptions.ProtocolError("connection broken"),
    ])
    resumed = FakeStream([b'{"seq":"2","id":"b","changes":[]}\n'])
    feed = continuous_feed([dropped, resumed])
    rows = []
    with mock.patch("couchdb_sdk.changes.time.sleep") as sleep:
        for row in feed:
            rows.append(row)
            if len(rows) == 2:
                feed.stop()
    assert [r["id"] for r in rows] == ["a", "b"]
    # Reconnected from the last seen seq, not from the start.
    assert feed._open.call_count == 2
    assert feed.since == "2"
    sleep.assert_called_once()


def test_continuous_raises_on_fatal_status():
    from couchdb_sdk import errors

    feed = continuous_feed([FakeStream([], status=404, body=b'{"error":"not_found"}')])
    with pytest.raises(errors.CouchDBError) as exc:
        list(feed)
    assert exc.value.status == 404


def test_continuous_rejects_filters():
    from couchdb_sdk.changes import ChangesFeed

    db = mock.Mock()
    with pytest.raises(ValueError):
        ChangesFeed(db, feed="continuous", selector={"t": 1})
