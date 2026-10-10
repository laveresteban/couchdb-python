# Changelog

## 0.5.0 (unreleased)
- Spec 0.5.0 adds `GET _all_docs`, `_design_docs`, `_bulk_get`, `_revs_diff`, `_explain`, `_purge`, `_compact`, `_active_tasks`, `_dbs_info`, `_scheduler/jobs|docs` and `_node/{node}/_config`.
- `HEAD` on documents, `open_revs`/`revs`/`attachments`/`latest` on `GET` document, ETag and X-Couch-Request-ID headers. Replication endpoints may be a string or an object.
- Reads (GET/HEAD) retry on 429, 502, 503, 504 and connection errors, honoring `Retry-After`; `CouchDB(max_retries=3)`. Writes are never retried.
- Transport failures raise `CouchDBError` with status 0.
- `Database.exists()` and revision lookups use HEAD instead of a full GET.
- `Database.iter_all_docs()` and `iter_find()` page through results; `bulk_get()`, `revs_diff()`, `purge()`, `explain()`, `design_docs()`, `compact()`.
- `CouchDB.dbs_info()`, `active_tasks()`, `scheduler_jobs()`, `scheduler_docs()`, `node_config()`.
- Fixed: a continuous feed with `seq_interval` lost its position when `seq` was null.
- Fixed: a continuous feed ignored `Retry-After` on error responses.
- Fixed: `stop()` on a continuous feed did not save the checkpoint for rows already delivered.

## 0.4.0 (unreleased)
- `Database.follow(feed="continuous")` reads the changes stream line by line.

## 0.3.0 (unreleased)
- `Database.follow()`: longpoll changes reader with jittered backoff, `Retry-After` and `_local` checkpoints.
- `Database.changes()` accepts `doc_ids` / `selector` and all feed options.
- `Database.get_local()` / `put_local()`.

## 0.1.0 (unreleased)
- Initial SDK generated from couchdb-openapi.
