# Architecture

The backend is a Django/DRF application under `backend/hangry_api`. Delivery, subtotal, tax, and total calculations are plain controller classes in `api/controllers.py`, exposed through API views. The frontend is React; Jest covers component behavior and Cypress covers browser acceptance flows.

The delivery API delegates fee calculation to `Delivery.calculate(order, distance)`.
