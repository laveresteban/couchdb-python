"""Typed CouchDB errors, translated from the generated client's ApiException."""
from __future__ import annotations

import contextlib
import json
from typing import Any, Iterator

from couchdb_client.exceptions import ApiException


class CouchDBError(Exception):
    def __init__(self, status: int, error: str, reason: str) -> None:
        super().__init__(f"{status} {error}: {reason}")
        self.status = status
        self.error = error
        self.reason = reason
        self.headers: Any = {}


class Unauthorized(CouchDBError):
    pass


class Forbidden(CouchDBError):
    pass


class NotFound(CouchDBError, KeyError):
    def __str__(self) -> str:  # KeyError would otherwise repr() the message
        return CouchDBError.__str__(self)


class Conflict(CouchDBError):
    pass


class PreconditionFailed(CouchDBError):
    pass


_BY_STATUS = {
    401: Unauthorized,
    403: Forbidden,
    404: NotFound,
    409: Conflict,
    412: PreconditionFailed,
}


def from_api_exception(exc: ApiException) -> CouchDBError:
    status = exc.status or 0
    error, reason = str(exc.reason or ""), str(exc.body or "")
    try:
        body = json.loads(exc.body or "")
        error, reason = body.get("error", error), body.get("reason", reason)
    except (TypeError, ValueError, AttributeError):
        pass
    err = _BY_STATUS.get(status, CouchDBError)(status, error, reason)
    err.headers = exc.headers or {}
    return err


@contextlib.contextmanager
def translate() -> Iterator[None]:
    """Re-raise generated-client ApiExceptions as typed CouchDBErrors."""
    try:
        yield
    except ApiException as exc:
        raise from_api_exception(exc) from None
