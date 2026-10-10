# Changelog

## 0.6.0 (unreleased)
- Regenerated from couchdb-openapi 0.6.0 (`_revs_diff`, `_bulk_get`, `revs`/`latest`
  on document GET, more view query fields, typed 401/403 responses).
- `Database.revs_diff()`, `bulk_get()`, `delete_local()` and `bulk_save(new_edits=False)`.
- `bulk_save()` now sets `_id`/`_rev` on the docs it saved, like `save()`.
- Continuous `follow()` accepts `doc_ids`/`selector`, encodes database names,
  and handles `"seq": null` rows from `seq_interval`.
- Cookie sessions renew themselves and log in again once after expiry.
- Only network errors, 429 and 5xx are retried (not bad URLs).
- `CouchDB(replication_url=...)` for servers that see themselves under a different host.
- Conformance fails when any scenario is skipped.

## 0.4.0 (unreleased)
- `follow(feed="continuous")`: streaming changes reader with heartbeats and reconnect.

## 0.3.0 (unreleased)
- `Database.follow()`: longpoll changes reader with jittered backoff, `Retry-After` and `_local` checkpoints.
- `Database.changes()` accepts `doc_ids` / `selector` and all feed options.
- `Database.get_local()` / `put_local()`.

## 0.1.0 (unreleased)
- Initial SDK generated from couchdb-openapi.
