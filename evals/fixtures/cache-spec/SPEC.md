# In-memory cache spec (confirmed)

- Three operations: `get(key)`, `set(key, value)`, `invalidate(key)`.
- Each entry expires `ttl` seconds after it is written; reading an expired entry returns `None` and must never return the old value.
- Capacity limit `capacity`; when exceeded, evict the least recently used entry (LRU). A `get` hit counts as a use.
- The time source is injectable for testing.
- Single-process use: no thread safety, persistence or distribution needed.
- The project has no usable cache dependency; use the standard library only.
