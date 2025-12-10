
// Modular import of frontend components
import { fetchVersion } from './components/version.js';
import { checkBackend } from './components/backendStatus.js';
import { checkForUpdates, getLatestRelease } from './components/update.js';

document.getElementById('check-backend').addEventListener('click', checkBackend);
window.addEventListener('DOMContentLoaded', fetchVersion);

// --- Update System UI Logic ---
const checkUpdatesBtn = document.getElementById('check-updates');
const updateNowBtn = document.getElementById('update-now');
const updateStatusDiv = document.getElementById('update-status');

checkUpdatesBtn.addEventListener('click', () => checkForUpdates(updateStatusDiv, updateNowBtn));

updateNowBtn.addEventListener('click', async () => {
    const latestRelease = getLatestRelease();
    if (!latestRelease || !latestRelease.assets || latestRelease.assets.length === 0) {
        updateStatusDiv.textContent = 'No downloadable update found.';
        return;
    }
    const asset = latestRelease.assets[0];
    updateStatusDiv.textContent = 'Downloading update...';
    try {
        // Download via backend proxy endpoint to avoid CORS issues
        const downloadUrl = `/api/download-update?asset_url=${encodeURIComponent(asset.browser_download_url)}`;
        // Create a hidden link and trigger download
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = asset.name;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        updateStatusDiv.innerHTML = `Update downloaded: <b>${asset.name}</b><br>Follow the instructions in the README or release notes to apply the update.`;
    } catch (err) {
        updateStatusDiv.textContent = 'Failed to download update.';
    }
});