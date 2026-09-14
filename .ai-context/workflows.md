# Workflows

Backend unit workflow: from `backend/hangry_api`, run `python -m pytest tests -p no:cacheprovider`. For focused coverage, run `coverage run --source=./api -m pytest tests -p no:cacheprovider` followed by `coverage report`.

Frontend workflows remain Jest for functional tests and Cypress for browser acceptance tests.
