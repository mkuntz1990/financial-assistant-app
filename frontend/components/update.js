// components/update.js
// Handles update check and UI logic

let latestRelease = null;

export async function checkForUpdates(updateStatusDiv, updateNowBtn) {
    updateStatusDiv.textContent = 'Checking for updates...';
    updateNowBtn.disabled = true;
    try {
        const response = await fetch('http://localhost:5000/api/latest-release');
        if (!response.ok) throw new Error('Failed to fetch release info');
        const data = await response.json();
        latestRelease = data;
        if (data.error) {
            updateStatusDiv.textContent = 'Error: ' + data.error;
            return;
        }
        // Compare with current version (implement as needed)
        updateStatusDiv.textContent = 'Latest release: ' + (data.tag_name || 'unknown');
        updateNowBtn.disabled = false;
    } catch (err) {
        updateStatusDiv.textContent = 'Could not check for updates.';
    }
}

export function getLatestRelease() {
    return latestRelease;
}
