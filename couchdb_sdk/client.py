"""Server-level entry point for the hand-written CouchDB SDK."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import couchdb_client as gen

from .database import Database
from .errors import NotFound, translate


class CouchDB:
    """Connect to a CouchDB server.

    >>> with CouchDB("http://localhost:5984", "admin", "password") as couch:
    ...     db = couch.create_database("people")
    ...     db["alice"] = {"age": 30}
    """

    def __init__(self, url: str = "http://localhost:5984",
                 username: Optional[str] = None, password: Optional[str] = None) -> None:
        config = gen.Configuration(host=url.rstrip("/"), username=username, password=password)
        self.client = gen.ApiClient(config)
        self._server = gen.ServerApi(self.client)
        self._auth = gen.AuthenticationApi(self.client)
        self._dbs = gen.DatabasesApi(self.client)
        self._replication = gen.ReplicationApi(self.client)

    def __enter__(self) -> "CouchDB":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def close(self) -> None:
        self.client.rest_client.pool_manager.clear()

    # -- server -----------------------------------------------------------
    def info(self) -> Dict[str, Any]:
        with translate():
            return self._server.get_server_information().to_dict()

    def up(self) -> bool:
        try:
            with translate():
                return self._server.get_up().status == "ok"
        except NotFound:
            return False

    def uuids(self, count: int = 1) -> List[str]:
        with translate():
            return self._server.get_uuids(count=count).uuids

    def all_dbs(self) -> List[str]:
        with translate():
            return self._server.get_all_dbs()

    # -- sessions ---------------------------------------------------------
    def login(self, name: str, password: str) -> None:
        """Start a cookie session; later requests send the AuthSession cookie."""
        with translate():
            res = self._auth.post_session_with_http_info(
                gen.SessionRequest(name=name, password=password))
        cookie = (res.headers or {}).get("Set-Cookie") or (res.headers or {}).get("set-cookie", "")
        self.client.cookie = cookie.split(";", 1)[0]

    def logout(self) -> None:
        with translate():
            self._auth.delete_session()
        self.client.cookie = None

    def session(self) -> Dict[str, Any]:
        with translate():
            info = self._auth.get_session()
        data = info.to_dict()
        data["userCtx"].setdefault("name", None)
        return data

    # -- databases --------------------------------------------------------
    def create_database(self, name: str, partitioned: bool = False) -> Database:
        with translate():
            self._dbs.put_database(name, partitioned=partitioned or None)
        return self[name]

    def delete_database(self, name: str) -> None:
        with translate():
            self._dbs.delete_database(name)

    def __getitem__(self, name: str) -> Database:
        return Database(self.client, name)

    def __contains__(self, name: object) -> bool:
        return self[str(name)].exists()

    # -- replication ------------------------------------------------------
    def _db_url(self, name: str) -> Dict[str, Any]:
        """Replication endpoint for a local database, carrying our credentials."""
        cfg = self.client.configuration
        endpoint: Dict[str, Any] = {"url": f"{cfg.host}/{name}"}
        if cfg.username:
            endpoint["auth"] = {"basic": {"username": cfg.username, "password": cfg.password}}
        return endpoint

    def replicate(self, source: str, target: str, **options: Any) -> Dict[str, Any]:
        """Replicate between databases. Bare names are resolved against this server."""
        def endpoint(x: str) -> Dict[str, Any]:
            return {"url": x} if "://" in x else self._db_url(x)

        body = {"source": endpoint(source), "target": endpoint(target), **options}
        with translate():
            return self._replication.post_replicate(gen.ReplicationRequest.from_dict(body)).to_dict()
