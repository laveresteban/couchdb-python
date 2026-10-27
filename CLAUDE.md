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

- Open fixes and planned features live in `ROADMAP.md`. Remove items there
  as they ship and note them in `CHANGELOG.md`.
