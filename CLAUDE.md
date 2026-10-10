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

- CI is the shared `sdk-ci.yml` in couchdb-sdk-generator (tests, conformance,
  generated-code drift check). Change it there, not here; `ci.yml` only
  passes this SDK's versions and commands. Behavior shared with the other
  SDKs is described in couchdb-sdk-generator `docs/sdk-design.md`.

- `from_dict` is safe for models with untyped fields since 0.7.0 (the
  generator's Python template only sets keys that are present); older
  wrapper code builds them with constructors, which is also fine.
- Wrap every generated call in `with translate():` so users get typed errors.

## Fixes still open

Done in 0.6.0/0.7.0: regenerated client, `sync.spec` steps and the 0.7.0
scenarios (46/46), continuous feed encoding/filters/null seqs, session
renewal, `bulk_save` revs, narrower `is_transient`, `replication_url`,
`head`/ETag, maintenance and listing helpers. `scripts/conformance.sh` fails
on skipped scenarios (Gauge alone reports them as a pass).

- The continuous reader doesn't log in again on a 401 mid-stream; it raises.

## Features to add

- Async client (`httpx` or the generator's `asyncio` library option).
- `__contains__` via `head()` instead of a full GET.
- Attachment streaming (no full `bytes` in memory for large files).
- `iter_all_docs()` / `iter_find()` helpers that page with bookmark/startkey.
- Type hints for documents (`TypedDict` or generic `Database[T]`).
