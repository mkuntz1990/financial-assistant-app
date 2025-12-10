# api/update.py
import os
import httpx
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

GITHUB_OWNER = "mkuntz1990"
GITHUB_REPO = "financial-assistant-app"

router = APIRouter()

@router.get("/api/latest-release")
async def latest_release():
    """
    Returns info about the latest GitHub release for this app.
    Useful for in-app update checks.
    """
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=10)
        if resp.status_code != 200:
            return {"error": "Could not fetch release info", "status_code": resp.status_code}
        data = resp.json()
        return {
            "tag_name": data.get("tag_name"),
            "name": data.get("name"),
            "body": data.get("body"),
            "html_url": data.get("html_url"),
            "published_at": data.get("published_at"),
            "assets": [
                {
                    "name": asset.get("name"),
                    "browser_download_url": asset.get("browser_download_url")
                } for asset in data.get("assets", [])
            ]
        }

@router.get("/api/download-update")
async def download_update(asset_url: str):
    """
    Streams the update asset from GitHub to the client.
    asset_url: direct download URL from GitHub release asset
    """
    if not asset_url.startswith("https://"):
        return {"error": "Invalid asset URL"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(asset_url, timeout=60)
        if resp.status_code != 200:
            return {"error": "Failed to download asset", "status_code": resp.status_code}
        filename = asset_url.split("/")[-1]
        headers = {"Content-Disposition": f"attachment; filename={filename}"}
        return StreamingResponse(resp.aiter_bytes(), headers=headers)
