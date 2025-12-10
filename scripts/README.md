# Scripts Directory

This directory is for utility scripts, deployment scripts, and automation tools related to the project.

## Ultra-Deploy Script

**File:** `ultra_deploy.ps1`

### What it does
- Bumps the patch version in `version.txt`
- Appends a new entry to `CHANGELOG.md` with the version and release message
- Commits and pushes changes to GitHub
- Creates a new GitHub release (if the GitHub CLI `gh` is installed)

### Usage
1. Open PowerShell in the project root.
2. Run:
	```powershell
	./scripts/ultra_deploy.ps1 -ReleaseMessage "Your release notes here"
	```
	- The `-ReleaseMessage` parameter is optional.
3. The script will display progress and any errors.

#### Prerequisites
- PowerShell (Windows)
- Git installed and configured
- GitHub CLI (`gh`) installed and authenticated (for release automation)

**Note:** The script is designed for modularity and can be extended for additional automation tasks as needed.