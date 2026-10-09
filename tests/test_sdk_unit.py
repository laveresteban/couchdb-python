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
