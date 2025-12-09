# NEW_PROJECT_SETUP_ROADMAP.md

## ⚡️ Project Setup Roadmap: Python+HTML Local Web App with Ultra-Deploy & Auto-Update

---


## PROJECT SETUP BEST PRACTICES

- Use clear, modular folder and file structure
- Write clean, well-commented code
- Add basic documentation for each setup step
- Ensure all scripts and configuration files are easy to understand and maintain

---

## PHASE 1: Project Initialization
- [x] Create project folder structure (backend, frontend, scripts, docs)
- [x] Initialize git repository and connect to GitHub
- [ ] Add .gitignore, README.md, and LICENSE
- [ ] Set up Python virtual environment and requirements.txt
- [ ] Set up basic Flask or FastAPI backend (serves static frontend)
- [ ] Set up basic HTML/CSS/JS frontend (landing page, connects to backend)
- [ ] Add initial test data (realistic for a $60k/year family)

## PHASE 2: Ultra-Deploy System
- [ ] Create ultra-deploy script (PowerShell or Bash)
- [ ] Script bumps version, commits, pushes, and creates GitHub release
- [ ] Add changelog and version tracking
- [ ] Document ultra-deploy usage in README

## PHASE 3: In-App Update System
- [ ] Backend endpoint to check for latest GitHub release
- [ ] Frontend UI for "Check for Updates" and "Update Now"
- [ ] Download and apply update (manual or guided)
- [ ] Document update process for users

## PHASE 4: Offline-First & Modularity
- [ ] Ensure all core features work offline
- [ ] Modularize backend and frontend code (folders, components, blueprints)
- [ ] Add/update test data for new features
- [ ] Document modular design in README

---

## HOW TO USE THIS ROADMAP

- To work on the next unchecked item, paste this statement to Copilot:

  **"Let's work on the next unchecked item (only that one) on the NEW_PROJECT_SETUP_ROADMAP.md. Make sure with me before you start that you are going to work on the correct item. Be sure to update test data at the end if necessary to test the new feature. The test data needs to be realistic for a family that only makes around 60k a year right now combined (the data doesn't have to be replaced from what was made in the past, instead just add some more data so it can test this new feature). Also be sure to maintain the modular design. Do all of this for me, keep everything according to the critical implementation instructions in the roadmap on lines 8-136. Do not stop during the implementation to ask me what I want to do, just do what you think is appropriate for that step (don't ask me what I want to do, tell me what I need to do). Also make sure to keep to the same type of 'theme' or complexity as the rest of the app that is already created."**

---

- To work on the next unchecked item in the financial assistant roadmap, use:

  **"Let's work on the next unchecked item (only that one) on the FINANCIAL_ASSISTANT_ROADMAP.md. Make sure with me before you start that you are going to work on the correct item. Be sure to update test data at the end if necessary to test the new feature. The test data needs to be realistic for a family that only makes around 60k a year right now combined (the data doesn't have to be replaced from what was made in the past, instead just add some more data so it can test this new feature). Also be sure to maintain the modular design. Do all of this for me, keep everything according to the critical implementation instructions in the roadmap on lines 8-136. Do not stop during the implementation to ask me what I want to do, just do what you think is appropriate for that step (don't ask me what I want to do, tell me what I need to do). Also make sure to keep to the same type of 'theme' or complexity as the rest of the app that is already created."**

---

- You can use these statements for any roadmap in this project. Copilot will check off each item as it is completed, following all standards and updating test data as needed.
