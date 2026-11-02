
# PowerShell System Monitoring & Administration

> CNET 334 — System Scripting | Centennial College

## Overview

This project documents the PowerShell system management concepts practiced during my CNET 334 coursework at Centennial College.

The objective was to retrieve Windows system information, inspect logged-on users, monitor services and processes, and test network connectivity using PowerShell commands.

The `system-report.ps1` script combines the commands from my completed Lab 2 into a single system information report.

The original lab was completed interactively using Windows PowerShell 5.1. The script was subsequently reconstructed from my saved lab transcript and successfully tested.

## Technologies

- Windows PowerShell 5.1
- Windows Management Instrumentation (WMI/CIM)
- PowerShell Cmdlets
- Pipelines and Object Filtering
- Windows Services and Processes
- ICMP Network Diagnostics

## Lab Objectives

- [x] Retrieve computer hardware and system information
- [x] Examine logged-on Windows users
- [x] Display the current date and time
- [x] Identify running Windows services
- [x] Sort processes by accumulated CPU time
- [x] Verify network connectivity using ICMP
- [x] Record the PowerShell session using transcripts
- [x] Reconstruct and execute the commands in a PowerShell script

## PowerShell Commands

### 1. Computer Information

```powershell
Get-CimInstance -ClassName Win32_ComputerSystem
```

Retrieves computer details, including manufacturer, model, domain, and installed physical memory.

### 2. Logged-on Users

```powershell
Get-CimInstance -ClassName Win32_LoggedOnUser
```

Displays associations between Windows user accounts and active logon sessions.

### 3. Date and Time

```powershell
Get-Date
```

Retrieves the current system date and time.

### 4. Running Windows Services

```powershell
Get-Service |
    Where-Object Status -EQ "Running" |
    Select-Object -Last 3
```

Retrieves Windows services, filters those currently running, and displays the last three entries.

### 5. Processes by CPU Time

```powershell
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 5
```

Displays the five processes with the highest accumulated CPU time.

**Note:** The `CPU` property represents total processor time consumed rather than instantaneous CPU utilization.

### 6. Network Connectivity

```powershell
Test-Connection www.google.com, www.amazon.com -Count 1 -BufferSize 512
```

Sends one ICMP echo request with a 512-byte payload to each destination.

This command helps verify basic network reachability and measure response times.

## Troubleshooting

### PowerShell Version Compatibility

During the original lab, I attempted to use the `-TargetName` parameter with `Test-Connection`.

The command failed because this parameter was unavailable in the Windows PowerShell 5.1 environment used for the lab.

After consulting `Get-Help Test-Connection`, I corrected the syntax by supplying the destination names directly.

The corrected command executed successfully.

This demonstrated the importance of checking cmdlet parameters and understanding differences between PowerShell versions.

## Verification

| Task | Result | Evidence |
|---|---|---|
| Computer information | Successful | Lab transcript |
| Logged-on users | Successful | Lab transcript |
| Date and time | Successful | Lab transcript |
| Running services | Successful | Lab transcript |
| CPU-time process sorting | Successful | Lab transcript |
| Network connectivity | Successful | Lab transcript |
| Combined script execution | Successful | Locally tested |

The original PowerShell commands were verified through my Lab 2 transcript.

The reconstructed `system-report.ps1` script was also successfully executed in a Windows PowerShell environment.

The original transcript is not included publicly because it contains personal and machine-specific information.

## Running the Script

The PowerShell script is available in this directory:

[`system-report.ps1`](system-report.ps1)

### Requirements

- Windows operating system
- Windows PowerShell 5.1 or a compatible PowerShell environment
- Network connectivity for the ICMP tests

### Execution

Open PowerShell, navigate to the directory containing the script, and execute:

```powershell
.\system-report.ps1
```

The script retrieves system information without modifying Windows settings.

Output varies depending on the computer, running services, processes, and network environment.

ICMP requests may fail if blocked by the destination or network firewall.

## Key Takeaways

This lab helped me become more comfortable using PowerShell for Windows system administration.

I learned how to retrieve system information through CIM, inspect services and processes, filter and sort objects using pipelines, and perform network connectivity tests.

One important lesson was understanding how PowerShell commands return objects that can be processed using additional cmdlets.

I also gained experience troubleshooting incorrect commands by consulting PowerShell's built-in help system.

Reconstructing the original lab commands into a single executable script helped reinforce these concepts and demonstrated how individual administrative commands can be combined into a reusable system reporting tool.

---

**Status:** Completed — Lab Verified & Script Tested Successfully

**Course:** CNET 334 — System Scripting

**Institution:** Centennial College
