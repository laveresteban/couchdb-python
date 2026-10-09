"""Long-running changes feed reader with retries and optional checkpoints."""
from __future__ import annotations

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
    """Follow `db`'s changes forever using longpoll.

    Transient failures are retried with jittered exponential backoff, or after
    the server's `Retry-After`, capped at `max_backoff`. With
    `checkpoint`, the position is stored in `_local/<checkpoint>` after each
    batch is consumed, so a restarted reader resumes where it left off
    (at-least-once delivery). `stop()` ends iteration after the current poll.

    >>> for change in db.follow(checkpoint="indexer", include_docs=True):
    ...     handle(change)
    """

    def __init__(self, db: "Database", since: str = "0", checkpoint: Optional[str] = None,
                 timeout: int = 60_000, batch_size: int = 500, max_retries: Optional[int] = None,
                 max_backoff: float = 30.0, **params: Any) -> None:
        self.db = db
        self.since = since
        self.checkpoint = checkpoint
        self.timeout = timeout
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.max_backoff = max_backoff
        self.params = params
        self._stopped = False
        self._checkpoint_rev: Optional[str] = None

    def stop(self) -> None:
        self._stopped = True

    def _retry(self, fn: Callable[[], T]) -> T:
        attempt = 0
        while True:
            try:
                return fn()
            except Exception as exc:
                if not is_transient(exc) or attempt == self.max_retries:
                    raise
                delay = retry_after(exc)
                if delay is None:
                    delay = random.uniform(0.5, 1.0) * 2 ** attempt  # jitter spreads out retries
                time.sleep(min(self.max_backoff, delay))
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
        return self.db.changes(since=self.since, feed="longpoll", timeout=self.timeout,
                               limit=self.batch_size, _request_timeout=self.timeout / 1000 + 10,
                               **self.params)

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        if self.checkpoint:
            self._load_checkpoint()
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
