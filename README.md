# Financial Assistant App

A modular Python + HTML local web application for personal financial management, featuring ultra-deploy and auto-update capabilities.

## Project Structure
- `backend/`: Python backend (Flask or FastAPI)
- `frontend/`: HTML/CSS/JS frontend
- `scripts/`: Automation and deployment scripts
- `docs/`: Documentation

## Setup
See `NEW_PROJECT_SETUP_ROADMAP.md` for step-by-step instructions.


## Ultra-Deploy System

The project includes an **ultra-deploy script** for automated version bumping, changelog updates, git commits, pushes, and GitHub release creation.

### Usage

1. Ensure you have the following prerequisites:
	- PowerShell (Windows)
	- [GitHub CLI (`gh`)](https://cli.github.com/) installed and authenticated (for GitHub release automation)
	- Git installed and configured
2. From the project root, run:
	```powershell
	./scripts/ultra_deploy.ps1 -ReleaseMessage "Your release notes here"
	```
	- If no message is provided, a default will be used.
3. The script will:
	- Bump the patch version in `version.txt`
	- Append a new entry to `CHANGELOG.md`
	- Commit and push changes to GitHub
	- Create a new GitHub release (if `gh` is available)


## Update Process (Auto-Update)


The Financial Assistant App includes a built-in update system that allows you to check for, download, and apply the latest updates directly from the app interface.

## Modular Design

This project is structured for clarity, maintainability, and ease of extension:

### Backend
- All backend logic is organized in the `backend/` folder.
- API endpoints are modularized as separate routers in `backend/api/` (e.g., `ping.py`, `version.py`, `health.py`, `update.py`).
- The main backend app (`app.py`) imports and registers these routers for a clean separation of concerns.
- This design makes it easy to add new endpoints or update existing ones without affecting unrelated code.

### Frontend
- All frontend logic is in the `frontend/` folder.
- UI features are split into modular components in `frontend/components/` (e.g., `version.js`, `backendStatus.js`, `update.js`).
- The main frontend logic is in `app.js`, which imports and uses these components.
- Styles are separated in `style.css`.
- This modular approach allows for easy extension and maintenance of the UI.

For more details, see the `README.md` files in the `backend/` and `frontend/` folders.

### How to Check for Updates
1. Start the backend server (see backend/README.md for instructions).
2. Open the app in your browser (open `frontend/index.html`).
3. Go to the **App Updates** section.
4. Click **Check for Updates**. The app will connect to GitHub and check for the latest release.

### How to Download and Apply Updates
1. If a new version is available, the app will display the version and release notes.
2. Click **Update Now**. The latest release package will be downloaded automatically.
3. Follow the instructions in the downloaded file, release notes, or this README to apply the update:
	- Replace the old files with the new ones from the downloaded package.
	- Restart the backend server if necessary.
	- Review the `CHANGELOG.md` for details on what has changed.

> **Note:** The update process is currently manual/guided. Automated in-app update and apply may be added in the future.

For troubleshooting or more details, see the [GitHub Releases page](https://github.com/mkuntz1990/financial-assistant-app/releases) or contact the project maintainer.
