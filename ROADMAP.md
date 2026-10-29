# Roadmap

Planned work for couchdb-python, roughly in order. Behavior shared with the other
SDKs follows couchdb-sdk-generator `docs/sdk-design.md`.

## Fixes

- The continuous changes reader raises on a 401 mid-stream. It should log in
  again once and resume from its checkpoint, as the longpoll reader does.
- Test and document against CouchDB 3.5.2 instead of 3.4 (the shared CI
  default moves with couchdb-sdk-generator).

## Features

- Async client, using `httpx` or the generator's `asyncio` library option, with
  the same typed errors and retries as the sync client.
- `iter_all_docs()` and `iter_find()` helpers that page with `startkey` and `bookmark`.
- Attachment streaming, so large files are not held in memory as `bytes`.
- Type hints for documents (`TypedDict` or a generic `Database[T]`).
- `__contains__` via `head()` instead of a full GET.

## Releases and docs

- A docs site covering the idiomatic layer, alongside the generated API docs in `docs/`.
