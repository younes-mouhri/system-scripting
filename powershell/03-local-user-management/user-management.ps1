# CNET 334 - System Scripting
# Project 03 - Windows Local User & Group Management
# Author: Younes Mouhri
# Reconstructed from PowerShell Lab 4

$ErrorActionPreference = "Stop"

# Check for administrator privileges
$IsAdmin = ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $IsAdmin) {
    Write-Host "ERROR: Run PowerShell as Administrator." -ForegroundColor Red
    return
}

# Generate unique names to avoid modifying existing accounts
$Suffix = [guid]::NewGuid().ToString("N").Substring(0, 8)
$UserName = "LabUser_$Suffix"
$GroupName = "LabGroup_$Suffix"

$UserCreated = $false
$GroupCreated = $false

try {
    # 1. Create local user
    Write-Host "`n===== CREATE LOCAL USER ====="

    $Password = Read-Host "Enter a temporary password for the lab user" -AsSecureString

    New-LocalUser -Name $UserName `
        -Password $Password `
        -Description "Temporary PowerShell lab account"

    $UserCreated = $true

    # 2. Verify local user
    Write-Host "`n===== VERIFY LOCAL USER ====="
    Get-LocalUser -Name $UserName

    # 3. Create local group
    Write-Host "`n===== CREATE LOCAL GROUP ====="

    New-LocalGroup -Name $GroupName `
        -Description "Temporary PowerShell lab group"

    $GroupCreated = $true

    # 4. Add user to group
    Write-Host "`n===== ADD USER TO GROUP ====="

    Add-LocalGroupMember -Group $GroupName -Member $UserName

    # 5. Verify group membership
    Write-Host "`n===== VERIFY GROUP MEMBERSHIP ====="

    Get-LocalGroupMember -Group $GroupName

    Write-Host "`n===== VERIFICATION COMPLETE =====" -ForegroundColor Green

    Read-Host "Press Enter to remove the temporary lab user and group"
}
finally {
    # 6. Remove temporary lab resources
    Write-Host "`n===== CLEANUP ====="

    if ($GroupCreated) {
        Remove-LocalGroup -Name $GroupName
        Write-Host "Temporary group removed."
    }

    if ($UserCreated) {
        Remove-LocalUser -Name $UserName
        Write-Host "Temporary user removed."
    }

    Write-Host "`n===== END OF LAB ====="
}
