"""Hand-written, idiomatic CouchDB SDK built on the generated `couchdb_client`.

This package is never touched by the generator (see .openapi-generator-ignore).
"""
from . import errors
from .changes import ChangesFeed
from .client import CouchDB
from .database import ChangesResult, Database, FindResult, Partition
from .errors import Conflict, CouchDBError, Forbidden, NotFound, PreconditionFailed, Unauthorized

__all__ = [
    "ChangesFeed", "ChangesResult", "Conflict", "CouchDB", "CouchDBError", "Database", "FindResult",
    "Forbidden", "NotFound", "Partition", "PreconditionFailed", "Unauthorized", "errors",
]
