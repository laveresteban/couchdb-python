import os
import uuid

import pytest

import couchdb_client
from couchdb_sdk import CouchDB

URL = os.environ.get("COUCHDB_URL", "http://localhost:5984")
USER = os.environ.get("COUCHDB_USER", "admin")
PASSWORD = os.environ.get("COUCHDB_PASSWORD", "password")


def unique_name(prefix="test"):
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


@pytest.fixture(scope="session")
def api_client():
    config = couchdb_client.Configuration(host=URL, username=USER, password=PASSWORD)
    with couchdb_client.ApiClient(config) as client:
        yield client


@pytest.fixture
def db(api_client):
    """Raw database name, for tests of the generated client."""
    name = unique_name()
    dbs = couchdb_client.DatabasesApi(api_client)
    dbs.put_database(name)
    yield name
    dbs.delete_database(name)


@pytest.fixture
def couch():
    with CouchDB(URL, USER, PASSWORD) as c:
        yield c


@pytest.fixture
def database(couch):
    """A `couchdb_sdk.Database`, for tests of the hand-written layer."""
    name = unique_name()
    d = couch.create_database(name)
    yield d
    couch.delete_database(name)
