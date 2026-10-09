# Changelog

## 0.3.0 (unreleased)
- `Database.follow()`: longpoll changes reader with jittered backoff, `Retry-After` and `_local` checkpoints.
- `Database.changes()` accepts `doc_ids` / `selector` and all feed options.
- `Database.get_local()` / `put_local()`.

## 0.1.0 (unreleased)
- Initial SDK generated from couchdb-openapi.
