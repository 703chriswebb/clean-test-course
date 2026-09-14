# Current State

As of 2026-09-13, the default delivery fee is `$3.50`; higher tiers remain `$5.00` and `$7.50` under their existing item/distance rules. Backend unit tests pass: 10 passed. The requested change is implemented but not committed.

Next: review the diff, then commit if desired. Existing pytest cache directories have local permission issues, so test runs use an explicit tests path and disable pytest's cache provider.
