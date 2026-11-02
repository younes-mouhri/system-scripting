
# CNET 334 - System Scripting
# Labs 1 & 3 - File and Directory Management
# Author: Younes Mouhri
# Portfolio adaptation of completed coursework

# Create a unique workspace inside the Windows temporary directory.
$LabPath = Join-Path $env:TEMP ("PowerShellFileLab-" + [guid]::NewGuid().ToString("N"))

Write-Host "`n===== FILE MANAGEMENT LAB ====="

New-Item -Path $LabPath -ItemType Directory | Out-Null

# Start recording the session
$TranscriptPath = Join-Path $LabPath "session-transcript.txt"
Start-Transcript -Path $TranscriptPath

# 1. Create a directory and subdirectory
Write-Host "`n[1] Creating directories"

$MainFolder = Join-Path $LabPath "Projects"
$SubFolder = Join-Path $MainFolder "Documents"

New-Item -Path $MainFolder -ItemType Directory
New-Item -Path $SubFolder -ItemType Directory

# 2. Create a text file
Write-Host "`n[2] Creating a text file"

$TextFile = Join-Path $SubFolder "sample.txt"

New-Item -Path $TextFile -ItemType File

# 3. Write content to the file
Write-Host "`n[3] Writing file contents"

Set-Content -Path $TextFile -Value "PowerShell File Management Lab"

# 4. Read the file
Write-Host "`n[4] Reading file contents"

Get-Content -Path $TextFile

# 5. Display the directory structure
Write-Host "`n[5] Current directory structure"

Get-ChildItem -Path $MainFolder -Recurse

# 6. Move the text file
Write-Host "`n[6] Moving the text file"

Move-Item -Path $TextFile -Destination $MainFolder

# 7. Remove the now-empty subdirectory
Write-Host "`n[7] Removing the empty subdirectory"

Remove-Item -Path $SubFolder

# 8. Verify the final directory structure
Write-Host "`n[8] Final directory structure"

Get-ChildItem -Path $MainFolder -Recurse

# Stop recording the session
Stop-Transcript

Write-Host "`n===== LAB COMPLETE ====="
Write-Host "Lab files saved at: $LabPath"
