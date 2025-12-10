# Ultra-Deploy Script for Financial Assistant App
# This PowerShell script automates deployment: version bump, commit, push, and GitHub release.
# Usage: Run from project root in PowerShell


param(
    [string]$ReleaseMessage = "Auto-deploy release"
)

# Step 1: Bump patch version in version.txt
$versionFile = "version.txt"
$newVersion = ""
if (Test-Path $versionFile) {
    # Find the first non-comment line
    $version = Get-Content $versionFile | Where-Object { $_ -notmatch '^#' } | Select-Object -First 1
    if ($version -and ($version -match '^(\\d+)\\.(\\d+)\\.(\\d+)$')) {
        $parts = $version -split '\.'
        $parts[2] = [int]$parts[2] + 1
        $newVersion = "$($parts[0]).$($parts[1]).$($parts[2])"
        # Overwrite only the version line, keep comments if present
        $lines = Get-Content $versionFile
        $newLines = @()
        $versionWritten = $false
        foreach ($line in $lines) {
            if (-not $versionWritten -and $line -notmatch '^#') {
                $newLines += $newVersion
                $versionWritten = $true
            } else {
                $newLines += $line
            }
        }
        if (-not $versionWritten) { $newLines += $newVersion }
        Set-Content $versionFile $newLines
        Write-Host "Version bumped to $newVersion"
    } elseif ($version) {
        Write-Host "Invalid version format in version.txt: $version. Skipping bump."
        $newVersion = $version
    } else {
        Write-Host "No valid version found in version.txt. Skipping bump."
        $newVersion = "unknown"
    }
} else {
    Write-Host "No version.txt found. Skipping version bump."
    $newVersion = "unknown"
}

# Step 2: Append to CHANGELOG.md
$changelogFile = "CHANGELOG.md"
if (Test-Path $changelogFile -and $newVersion -ne "unknown") {
    Add-Content $changelogFile "`n## [$newVersion] - $(Get-Date -Format 'yyyy-MM-dd')`n- $ReleaseMessage`n"
    Write-Host "Changelog updated."
} else {
    Write-Host "No CHANGELOG.md found or version unknown. Skipping changelog update."
}

# Step 3: Git add, commit, push
& git add .
& git commit -m "Release ${newVersion}: $ReleaseMessage"
& git push

# Step 4: Create GitHub release (requires gh CLI)
if (Get-Command gh -ErrorAction SilentlyContinue -CommandType Application) {
    & gh release create $newVersion --title "Release $newVersion" --notes $ReleaseMessage
    Write-Host "GitHub release created: $newVersion"
} else {
    Write-Host "GitHub CLI (gh) not found. Skipping release creation."
}

# End of script
