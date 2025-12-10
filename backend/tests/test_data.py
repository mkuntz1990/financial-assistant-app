# Sample test data for backend API endpoints
# This file provides mock data and utility functions for testing backend features.

MOCK_VERSION_RESPONSE = {
    "version": "1.2.3",
    "release_date": "2025-12-01",
    "notes": "Test version for automated testing."
}

MOCK_UPDATE_RESPONSE = {
    "update_available": True,
    "latest_version": "1.2.3",
    "download_url": "https://example.com/download/1.2.3",
    "changelog": "- Bug fixes\n- Performance improvements"
}

MOCK_HEALTH_RESPONSE = {
    "status": "ok",
    "uptime": 123456,
    "timestamp": "2025-12-10T12:00:00Z"
}

MOCK_PING_RESPONSE = {
    "pong": True,
    "timestamp": "2025-12-10T12:00:00Z"
}

# Utility function for test clients
def get_mock_response(endpoint):
    if endpoint == "version":
        return MOCK_VERSION_RESPONSE
    elif endpoint == "update":
        return MOCK_UPDATE_RESPONSE
    elif endpoint == "health":
        return MOCK_HEALTH_RESPONSE
    elif endpoint == "ping":
        return MOCK_PING_RESPONSE
    else:
        return {}
