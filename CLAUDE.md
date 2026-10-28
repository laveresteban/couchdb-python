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

## Secure SDLC

- Follow secure SDLC when implementing: threat-model new network, auth, or
  file-handling code before writing it, and review the diff for injection,
  unsafe deserialization, path traversal, and credential leakage before
  committing.
- Every security-relevant change adds test cases that cover it: invalid or
  hostile input, auth failures (401/403), TLS and host handling, and
  error paths that must not leak credentials or server internals.
- Never log, print, or put credentials in URLs, exception messages, or
  test fixtures; use env vars or mocked values.
- Keep dependencies pinned to supported ranges and flag known-vulnerable
  versions in the PR description.

## Releasing

- Bump `VERSION` in `setup.py` to the spec version, and date the matching
  `CHANGELOG.md` heading. `couchdb_client/` and `.generated-from` come from a
  regeneration in couchdb-sdk-generator; the release check fails if they disagree.
- Merge to `main`, then push tag `v<version>`. The release workflow runs CI,
  then creates the GitHub Release (notes from CHANGELOG) and publishes to PyPI.
