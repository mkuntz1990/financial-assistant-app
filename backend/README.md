# Project Folder Structure

This directory contains the main modules for the backend of the Financial Assistant App. Place all backend-related code (APIs, business logic, models, etc.) here.

## Modular Design

- API endpoints are organized as separate routers in the `api/` folder (e.g., `ping.py`, `version.py`, `health.py`, `update.py`).
- The main backend app (`app.py`) imports and registers these routers for a clean, modular structure.
- This makes it easy to add or update endpoints without affecting other parts of the backend.
