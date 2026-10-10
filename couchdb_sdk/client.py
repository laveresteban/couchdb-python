"""Server-level entry point for the hand-written CouchDB SDK."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from urllib.parse import quote

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
                 username: Optional[str] = None, password: Optional[str] = None,
                 replication_url: Optional[str] = None) -> None:
        """`replication_url` is how the CouchDB server reaches itself, for
        `replicate()` with bare database names. It defaults to `url`; set it
        when the client and server see different hostnames (Docker, proxies)."""
        config = gen.Configuration(host=url.rstrip("/"), username=username, password=password)
        self.client = gen.ApiClient(config)
        self.replication_url = (replication_url or url).rstrip("/")
        self._credentials: Optional[Tuple[str, str]] = None
        self._hook_session()
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
    def _hook_session(self) -> None:
        """Keep the cookie session alive.

        CouchDB re-issues `Set-Cookie` as the session nears expiry; keep the
        newest one. If the session expired anyway (401 while sending a
        cookie), log in again once and retry the request.
        """
        rest = self.client.rest_client
        send = rest.request

        def request(method: str, url: str, headers: Optional[Dict[str, Any]] = None,
                    *args: Any, **kwargs: Any) -> Any:
            res = send(method, url, headers, *args, **kwargs)
            if (res.status == 401 and self._credentials and headers and headers.get("Cookie")
                    and not url.rstrip("/").endswith("/_session")):
                res.response.drain_conn()
                self.login(*self._credentials)
                res = send(method, url, dict(headers, Cookie=self.client.cookie), *args, **kwargs)
            self._keep_cookie(res.getheader("Set-Cookie"))
            return res

        rest.request = request

    def _keep_cookie(self, header: Optional[str]) -> None:
        kv = (header or "").split(";", 1)[0]
        if kv.startswith("AuthSession=") and len(kv) > len("AuthSession=") and self._credentials:
            self.client.cookie = kv

    def login(self, name: str, password: str) -> None:
        """Start a cookie session; later requests send the AuthSession cookie.

        The session is renewed automatically while the client is in use.
        """
        with translate():
            res = self._auth.post_session_with_http_info(
                gen.SessionRequest(name=name, password=password))
        cookie = (res.headers or {}).get("Set-Cookie") or (res.headers or {}).get("set-cookie", "")
        self.client.cookie = cookie.split(";", 1)[0]
        self._credentials = (name, password)

    def logout(self) -> None:
        self._credentials = None
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
        endpoint: Dict[str, Any] = {"url": f"{self.replication_url}/{quote(name, safe='')}"}
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
