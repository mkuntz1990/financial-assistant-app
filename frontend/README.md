# Frontend

This folder contains the HTML/CSS/JS landing page for the Financial Assistant App.

## Files
- `index.html`: Main landing page
- `style.css`: Basic styles
- `app.js`: Handles backend connection and UI logic

## How it works
- Open `index.html` in your browser
- Click "Check Backend Connection" to test communication with the backend (`/ping` endpoint)
- Ensure backend is running locally (default: http://localhost:5000)

## Best Practices


### Modular Design & Usage


#### Backend Connection

#### Next Steps
Keep UI modular and simple
Document all major changes
Use clear comments in code

---

## Modular Design

- UI features are split into modular components in the `components/` folder (e.g., `version.js`, `backendStatus.js`, `update.js`).
- All frontend logic is in `app.js`, which imports and uses these components.
- Styles are separated in `style.css` for clarity.
- The landing page is minimal and ready for extension.

---

### Modular Design & Usage

- All frontend logic is in `app.js` for easy maintenance.
- Styles are separated in `style.css` for clarity.
- The landing page is minimal and ready for extension.

#### Backend Connection
- The button in the UI sends a request to `/ping` on the backend.
- Backend should respond with `{ message: "pong" }` for successful connection.

#### Next Steps
- Expand UI components as needed.
- Connect additional endpoints for more features.