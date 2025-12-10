// components/backendStatus.js
// Handles backend connection check

export async function checkBackend() {
    const statusDiv = document.getElementById('backend-status');
    statusDiv.textContent = 'Checking...';
    try {
        const response = await fetch('http://localhost:5000/ping');
        if (response.ok) {
            const data = await response.json();
            statusDiv.textContent = 'Backend is online: ' + (data.message || 'Success');
        } else {
            statusDiv.textContent = 'Backend responded with error.';
        }
    } catch (err) {
        statusDiv.textContent = 'Could not connect to backend.';
    }
}
