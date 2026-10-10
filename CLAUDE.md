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

## Fixes

1. **Generated client is on spec 0.4.0; spec is 0.5.0.** No `revs` / `latest`
   on `get_document`, no `post_revs_diff` / `post_bulk_get`. Regenerate.
   `CHANGELOG.md` also has no 0.4.0 entry for the continuous feed.
2. **`sync.spec` steps are missing**, so conformance will fail on its next
   run against generator `main`. Needs: revs diff, bulk get with history,
   local doc get/put/delete, write with `new_edits=false`, conflict count,
   `style=all_docs` changes, selector-filtered changes. Add the matching
   wrapper methods (`revs_diff`, `bulk_get`, `delete_local`,
   `bulk_save(new_edits=False)`) rather than calling the generated client
   from steps.
3. **Continuous feed URL isn't encoded.** `ChangesFeed._open` builds
   `f"{cfg.host}/{self.db.name}/_changes"`, so a db name like `a/b` or `a+b`
   hits the wrong path. Use `urllib.parse.quote(name, safe="")`.
4. **`seq_interval` breaks the continuous reader.** Rows can carry
   `"seq": null`; `row.get("seq", self.since)` then sets `since` to `None`
   and the next checkpoint or reconnect sends `since=None`. Keep the old value
   when seq is null.
5. **Continuous mode rejects `doc_ids`/`selector`.** It raises `ValueError`.
   CouchDB accepts POST `_changes?feed=continuous` with a body, so stream a
   POST instead.
6. **Cookie sessions never refresh.** `login()` stores the cookie once; it
   expires (10 min default) and later calls get 401. couchdb-node keeps the
   latest `Set-Cookie`. Do the same, and optionally re-login on 401 when the
   password is known.
7. **`bulk_save` doesn't update the input docs.** `save()` sets `_id`/`_rev`
   in place, `bulk_save()` doesn't, so a second `bulk_save` of the same list
   conflicts. Copy `id`/`rev` back for rows without `error`.
8. **`is_transient` treats every `urllib3.exceptions.HTTPError` as
   transient**, including `LocationParseError` and similar config errors, so a
   bad URL retries forever with `max_retries=None`. Narrow it to
   connection/timeout/protocol errors.
9. `replicate()` uses the client's host as the source/target URL. When
   the client talks to CouchDB through a different hostname (Docker,
   proxies), the server can't reach that URL. Let callers pass a server-side
   base URL.

## Features to add

- Async client (`httpx` or the generator's `asyncio` library option).
- `has()`/`__contains__` via `HEAD` once the spec has it.
- Attachment streaming (no full `bytes` in memory for large files).
- `Database.purge`, `explain`, `design_docs`, `local_docs` as the spec grows.
- `iter_all_docs()` / `iter_find()` helpers that page with bookmark/startkey.
- Type hints for documents (`TypedDict` or generic `Database[T]`).
