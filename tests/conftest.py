import os
import uuid

import pytest

import couchdb_client

URL = os.environ.get("COUCHDB_URL", "http://localhost:5984")
USER = os.environ.get("COUCHDB_USER", "admin")
PASSWORD = os.environ.get("COUCHDB_PASSWORD", "password")


@pytest.fixture(scope="session")
def api_client():
    config = couchdb_client.Configuration(host=URL, username=USER, password=PASSWORD)
    with couchdb_client.ApiClient(config) as client:
        yield client


@pytest.fixture
def db(api_client):
    name = f"test_{uuid.uuid4().hex[:12]}"
    dbs = couchdb_client.DatabasesApi(api_client)
    dbs.put_database(name)
    yield name
    dbs.delete_database(name)
