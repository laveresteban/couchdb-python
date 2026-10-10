# CLAUDE.md — couchdb-python

Python SDK, published as `couchdb-sdk`.

- `couchdb_client/` and `docs/`: generated. Never edit; regenerate from
  couchdb-sdk-generator (`npm run generate:python`).
- `couchdb_sdk/`: hand-written idiomatic layer (`client.py`, `database.py`,
  `changes.py`, `errors.py`).
- `conformance/step_impl/steps.py`: Gauge steps for the shared specs.
- Protected files are listed in `.openapi-generator-ignore`.

## Commands

```sh
docker run -d -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password couchdb:3.4
pip install -e . -r test-requirements.txt
pytest tests
bash scripts/conformance.sh [--tags sync]
```

## Rules

- Build request models with constructors, not `from_dict`, when they have
  untyped fields (see the comment in `database.py`).
- Wrap every generated call in `with translate():` so users get typed errors.

## Fixes still open

Done in 0.6.0: regenerated client, `sync.spec` steps, continuous feed
encoding/filters/null seqs, session renewal, `bulk_save` revs, narrower
`is_transient`, `replication_url`. `scripts/conformance.sh` now fails on
skipped scenarios (Gauge alone reports them as a pass).

- The continuous reader doesn't log in again on a 401 mid-stream; it raises.

## Features to add

- Async client (`httpx` or the generator's `asyncio` library option).
- `has()`/`__contains__` via `HEAD` once the spec has it.
- Attachment streaming (no full `bytes` in memory for large files).
- `Database.purge`, `explain`, `design_docs`, `local_docs` as the spec grows.
- `iter_all_docs()` / `iter_find()` helpers that page with bookmark/startkey.
- Type hints for documents (`TypedDict` or generic `Database[T]`).
