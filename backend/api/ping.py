# api/ping.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    """Endpoint for frontend connectivity test."""
    return {"message": "pong"}
