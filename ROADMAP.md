# Roadmap

Planned work for couchdb-python, roughly in order. Behavior shared with the other
SDKs follows couchdb-sdk-generator `docs/sdk-design.md`.

## In progress

- Require Python 3.11 (breaking) and run CI and docs on CouchDB 3.5.2
  (branch `fix/python-3.11-floor-couchdb-3.5.2`).

## Fixes

- The continuous changes reader raises on a 401 mid-stream. It should log in
  again once and resume from its checkpoint, as the longpoll reader does.

## Features

- Async client, using `httpx` or the generator's `asyncio` library option, with
  the same typed errors and retries as the sync client.
- `iter_all_docs()` and `iter_find()` helpers that page with `startkey` and `bookmark`.
- Attachment streaming, so large files are not held in memory as `bytes`.
- Type hints for documents (`TypedDict` or a generic `Database[T]`).
- `__contains__` via `head()` instead of a full GET.

## Releases and docs

- Publish each spec version to PyPI as `couchdb-sdk` (tag `v<spec_version>`).
- A docs site covering the idiomatic layer, alongside the generated API docs in `docs/`.
