# Test Data for Backend API

This directory contains mock data and sample responses for backend API endpoints, used for testing and development purposes.

- `test_data.py`: Provides mock responses for version, update, health, and ping endpoints.
- `test_api.py`: Example unit tests using the mock data.

## Usage

Import `test_data.py` in your backend tests to simulate API responses without hitting live endpoints. Run `test_api.py` with `python -m unittest backend/tests/test_api.py` to execute the sample tests.

This helps ensure new features are covered by test data and can be validated independently of the production environment.
