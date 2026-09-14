# Decisions

## 2026-09-13 — Default delivery fee

- Changed the base delivery fee from `$2.50` to `$3.50` in `Delivery.calculate`.
- Updated base-fee unit assertions, including empty-order and boundary cases.
- Retained pytest because it is already the backend CI/framework standard and is appropriate for this focused change; no framework migration was justified.
