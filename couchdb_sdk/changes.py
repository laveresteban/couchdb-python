"""Long-running changes feed reader with retries and optional checkpoints."""
from __future__ import annotations

import json
import random
import time
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterator, Optional, TypeVar

import urllib3

from .errors import CouchDBError, NotFound

if TYPE_CHECKING:
    from .database import Database

T = TypeVar("T")


def is_transient(exc: Exception) -> bool:
    """Network errors, 429 and 5xx are worth retrying; other errors are not."""
    if isinstance(exc, urllib3.exceptions.HTTPError):
        return True
    return isinstance(exc, CouchDBError) and (exc.status in (0, 429) or exc.status >= 500)


def retry_after(exc: Exception) -> Optional[float]:
    """Seconds from a `Retry-After` header, if the server sent one."""
    try:
        return float(exc.headers["Retry-After"])  # type: ignore[attr-defined]
    except (AttributeError, KeyError, TypeError, ValueError):
        return None


class ChangesFeed:
    """Follow `db`'s changes forever.

    `feed="longpoll"` (default) polls one batch at a time through the generated
    client. `feed="continuous"` holds one connection open and reads changes
    line by line as CouchDB emits them (lower latency); it reads the raw HTTP
    stream directly, since the generated client would wait for the whole body.

    Transient failures are retried with jittered exponential backoff, or after
    the server's `Retry-After`, capped at `max_backoff`. With `checkpoint`, the
    position is stored in `_local/<checkpoint>` as it advances, so a restarted
    reader resumes where it left off (at-least-once delivery). `stop()` ends
    iteration. `heartbeat` (ms) keeps an idle connection alive; continuous uses
    it to tell a quiet feed from a dead one and reconnect.

    >>> for change in db.follow(feed="continuous", include_docs=True):
    ...     handle(change)
    """

    def __init__(self, db: "Database", since: str = "0", checkpoint: Optional[str] = None,
                 feed: str = "longpoll", timeout: int = 60_000, heartbeat: Optional[int] = None,
                 batch_size: int = 500, max_retries: Optional[int] = None,
                 max_backoff: float = 30.0, **params: Any) -> None:
        if feed == "continuous" and ("doc_ids" in params or "selector" in params):
            raise ValueError("continuous feed cannot filter by doc_ids/selector; "
                             "use feed='longpoll'")
        self.db = db
        self.since = since
        self.checkpoint = checkpoint
        self.feed = feed
        self.timeout = timeout
        self.heartbeat = heartbeat
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.max_backoff = max_backoff
        self.params = params
        self._stopped = False
        self._checkpoint_rev: Optional[str] = None

    def stop(self) -> None:
        self._stopped = True

    def _backoff(self, attempt: int, exc: Exception) -> None:
        delay = retry_after(exc)
        if delay is None:
            delay = random.uniform(0.5, 1.0) * 2 ** attempt  # jitter spreads out retries
        time.sleep(min(self.max_backoff, delay))

    def _retry(self, fn: Callable[[], T]) -> T:
        attempt = 0
        while True:
            try:
                return fn()
            except Exception as exc:
                if not is_transient(exc) or attempt == self.max_retries:
                    raise
                self._backoff(attempt, exc)
                attempt += 1

    def _load_checkpoint(self) -> None:
        try:
            doc = self._retry(lambda: self.db.get_local(self.checkpoint))
        except NotFound:
            return
        self.since, self._checkpoint_rev = doc["since"], doc["_rev"]

    def _save_checkpoint(self) -> None:
        doc: Dict[str, Any] = {"since": self.since}
        if self._checkpoint_rev:
            doc["_rev"] = self._checkpoint_rev
        self._checkpoint_rev = self._retry(lambda: self.db.put_local(self.checkpoint, doc))["_rev"]

    def _poll(self) -> Any:
        # Read timeout must outlast the server's longpoll timeout.
        extra = {"heartbeat": self.heartbeat} if self.heartbeat is not None else {}
        return self.db.changes(since=self.since, feed="longpoll", timeout=self.timeout,
                               limit=self.batch_size, _request_timeout=self.timeout / 1000 + 10,
                               **extra, **self.params)

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        if self.checkpoint:
            self._load_checkpoint()
        if self.feed == "continuous":
            yield from self._stream()
            return
        while not self._stopped:
            res = self._retry(self._poll)
            for row in res.results:
                if self._stopped:
                    return
                yield row
            if res.last_seq != self.since:
                self.since = res.last_seq
                if self.checkpoint:
                    self._save_checkpoint()

    # -- continuous feed --------------------------------------------------
    def _open(self) -> Any:
        """Open a raw streaming GET on the continuous feed from self.since."""
        cfg = self.db.client.configuration
        hb = self.heartbeat if self.heartbeat is not None else 30_000
        fields: Dict[str, str] = {"feed": "continuous", "since": str(self.since),
                                  "heartbeat": str(hb)}
        for key, val in self.params.items():
            if val is None:
                continue
            fields[key] = "true" if val is True else "false" if val is False else str(val)
        headers: Dict[str, str] = {}
        token = cfg.get_basic_auth_token()
        if token:
            headers["Authorization"] = token
        cookie = getattr(self.db.client, "cookie", None)
        if cookie:
            headers["Cookie"] = cookie
        # Read timeout must outlast the heartbeat: a longer silence means a dead feed.
        timeout = urllib3.Timeout(connect=10.0, read=hb / 1000 + 10)
        return self.db.client.rest_client.pool_manager.request(
            "GET", f"{cfg.host}/{self.db.name}/_changes", fields=fields, headers=headers,
            preload_content=False, timeout=timeout, retries=False)

    @staticmethod
    def _lines(resp: Any) -> Iterator[bytes]:
        buf = b""
        for chunk in resp.stream(amt=8192, decode_content=True):
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                yield line

    def _stream(self) -> Iterator[Dict[str, Any]]:
        attempt = 0
        pending = 0  # rows yielded since the last checkpoint save
        while not self._stopped:
            try:
                resp = self._open()
                if resp.status >= 400:
                    err = CouchDBError(resp.status, "", resp.read().decode("utf-8", "replace"))
                    err.headers = resp.headers  # keeps Retry-After for the backoff
                    raise err
                attempt = 0  # a good connection resets the backoff
                try:
                    for line in self._lines(resp):
                        if self._stopped:
                            break  # fall through so the checkpoint still saves
                        if not line:  # blank line is a heartbeat
                            continue
                        row = json.loads(line)
                        if "last_seq" in row:  # end of this batch
                            self.since = row["last_seq"]
                            break
                        yield row
                        if row.get("seq") is not None:  # null when seq_interval skips it
                            self.since = row["seq"]
                        pending += 1
                        if self.checkpoint and pending >= self.batch_size:
                            self._save_checkpoint()
                            pending = 0
                finally:
                    resp.release_conn()
                if self.checkpoint and pending:
                    self._save_checkpoint()
                    pending = 0
            except Exception as exc:
                if self._stopped or not is_transient(exc) or attempt == self.max_retries:
                    raise
                self._backoff(attempt, exc)
                attempt += 1
