
# PowerShell File & Directory Management

> CNET 334 — System Scripting | Centennial College

## Overview

This project demonstrates basic filesystem administration using Windows PowerShell.

It combines the concepts covered in Labs 1 and 3 of my System Scripting coursework at Centennial College.

The objective was to create and manage directories, manipulate text files, verify filesystem changes, and record administrative sessions using PowerShell.

The `file-management.ps1` script automates these tasks in an isolated temporary workspace.

## Technologies

- Windows PowerShell
- PowerShell Cmdlets
- Windows Filesystem
- File and Directory Management
- PowerShell Transcripts

## Objectives

- [x] Create directories and subdirectories
- [x] Create a text file
- [x] Write content to a file
- [x] Read file contents
- [x] Display directory contents
- [x] Move files between directories
- [x] Remove an empty directory
- [x] Verify the final directory structure
- [x] Record the session using PowerShell transcripts
- [x] Execute and verify the completed script

## PowerShell Commands

| Cmdlet | Purpose |
|---|---|
| `New-Item` | Create files and directories |
| `Join-Path` | Construct filesystem paths |
| `Set-Content` | Write content into a file |
| `Get-Content` | Read file contents |
| `Get-ChildItem` | List files and directories |
| `Move-Item` | Move files |
| `Remove-Item` | Remove files or directories |
| `Start-Transcript` | Record a PowerShell session |
| `Stop-Transcript` | Stop recording the session |

## File Management Workflow

### 1. Directory Creation

The script creates a unique temporary workspace to avoid modifying existing personal files.

It then creates the following structure:

```text
Projects/
└── Documents/
```

### 2. File Creation and Modification

A text file named `sample.txt` is created inside the `Documents` directory.

The script writes the following content:

```text
PowerShell File Management Lab
```

The contents are verified using `Get-Content`.

### 3. File Movement

The text file is moved from `Documents` to its parent directory, `Projects`.

The now-empty `Documents` directory is removed.

### 4. Final Verification

The final directory structure is:

```text
Projects/
└── sample.txt
```

The directory contents are verified using `Get-ChildItem`.

## Troubleshooting

### PowerShell Execution Policy

During testing, PowerShell initially prevented the script from executing because script execution was disabled.

I inspected the execution policy and temporarily used `RemoteSigned` for the current session.

The script was subsequently blocked because it had been downloaded from GitHub and was not digitally signed.

After verifying the script's contents, I used:

```powershell
Unblock-File -Path .\file-management.ps1
```

This removed the downloaded-file security marker from the specific script without changing the system-wide execution policy.

The script then executed successfully.

This demonstrated how PowerShell execution policies affect script execution and how to troubleshoot these restrictions.

## Verification

The PowerShell script was successfully executed and tested
on a Windows environment.

| Test | Result |
|------|--------|
| Directory creation | Passed |
| File creation | Passed |
| Writing and reading file contents | Passed |
| Listing directory contents | Passed |
| Moving files between directories | Passed |
| Removing an empty directory | Passed |
| Final directory structure verification | Passed |

All file-management operations completed successfully.

## Running the Script

The script is available here:

[`file-management.ps1`](file-management.ps1)

### Requirements

- Windows operating system
- Windows PowerShell 5.1 or a compatible PowerShell environment

### Execution

Open PowerShell, navigate to the directory containing the script, and run:

```powershell
.\file-management.ps1
```

The script creates a uniquely named workspace in the Windows temporary directory.

It only removes the empty subdirectory created during execution.

The completed files and transcript remain available for inspection.

## Key Takeaways

This project helped me reinforce the fundamentals of filesystem administration using PowerShell.

I practiced creating and managing directories, manipulating file contents, and verifying filesystem changes.

Combining the exercises from Labs 1 and 3 into a single script demonstrated how individual administrative commands can be automated into a repeatable workflow.

I also gained practical troubleshooting experience with PowerShell execution policies and downloaded-script restrictions.

---

**Status:** Completed — Script Tested Successfully

**Course:** CNET 334 — System Scripting

**Institution:** Centennial College
