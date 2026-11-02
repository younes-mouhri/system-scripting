# CNET 334 - System Scripting
# Lab 2 - PowerShell System Management
# Author: Younes Mouhri
# Reconstructed from the original Lab 2 transcript

# 1. Computer Information
Write-Host "`n===== COMPUTER INFORMATION ====="
Get-CimInstance -ClassName Win32_ComputerSystem

# 2. Logged-on Users
Write-Host "`n===== LOGGED-ON USERS ====="
Get-CimInstance -ClassName Win32_LoggedOnUser

# 3. Current Date and Time
Write-Host "`n===== DATE AND TIME ====="
Get-Date

# 4. Last 3 Running Services
Write-Host "`n===== RUNNING SERVICES ====="
Get-Service |
    Where-Object Status -EQ "Running" |
    Select-Object -Last 3

# 5. Top 5 Processes by CPU Time
Write-Host "`n===== TOP 5 PROCESSES BY CPU TIME ====="
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 5

# 6. Network Connectivity Test
Write-Host "`n===== NETWORK CONNECTIVITY ====="
Test-Connection www.google.com, www.amazon.com -Count 1 -BufferSize 512

Write-Host "`n===== END OF REPORT ====="

