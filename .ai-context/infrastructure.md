# Infrastructure

Backend tests run locally from `backend/hangry_api` with Python and pytest. CI workflows install pytest, `django_mock_queries`, six, and coverage, then run backend tests from the `backend` directory. Coverage artifacts are generated locally and should not be included in the feature diff.
