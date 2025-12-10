# api/version.py
import os
from fastapi import APIRouter

router = APIRouter()

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), '..', '..', 'version.txt')
    try:
        with open(version_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    return line
    except Exception:
        return "unknown"

@router.get("/api/version")
def api_version():
    """Return current app version from version.txt"""
    return {"version": get_version()}
