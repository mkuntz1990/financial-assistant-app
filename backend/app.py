

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.ping import router as ping_router
from api.version import router as version_router
from api.health import router as health_router
from api.update import router as update_router

app = FastAPI()

# Serve static files from the frontend directory
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

# Register API routers
app.include_router(ping_router)
app.include_router(version_router)
app.include_router(health_router)
app.include_router(update_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
