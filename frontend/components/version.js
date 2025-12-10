// components/version.js
// Handles fetching and displaying the app version

export async function fetchVersion() {
    try {
        const response = await fetch('http://localhost:5000/api/version');
        if (response.ok) {
            const data = await response.json();
            document.getElementById('app-version').textContent = 'Version: ' + (data.version || 'unknown');
        } else {
            document.getElementById('app-version').textContent = 'Version: unknown';
        }
    } catch (err) {
        document.getElementById('app-version').textContent = 'Version: unavailable';
    }
}
