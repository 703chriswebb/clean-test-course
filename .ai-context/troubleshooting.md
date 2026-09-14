# Troubleshooting

## 2026-09-13 — pytest cache permission errors

Running pytest from the backend test root initially collected stale `pytest-cache-files-*` directories and failed with `PermissionError: [WinError 5] Access is denied`. Running an explicit `tests` path with `-p no:cacheprovider` bypassed those directories and allowed all 10 tests to pass. The stale directories were not part of the requested code change.
