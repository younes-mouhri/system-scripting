# Project 04 — Python System & Network Administration

## Overview

A Python scripting project developed from practical System Scripting labs at Centennial College.

This project brings together three areas of Python programming:

- **Python Modules:** Creating and importing reusable functions.
- **System Administration:** Managing directories, navigating the filesystem, and retrieving system information.
- **Networking:** Resolving hostnames, identifying network services, and converting IPv4 addresses into packed binary format.

The command-line tool brings together the module structure, filesystem inspection, and network lookups from Labs 5–7.

## Technologies

- Python 3
- PyCharm
- Windows 11
- Python Standard Library: `os`, `socket`, `datetime`

No external Python packages are required for the original lab functionality.

## 1. Python Modules & Functions — Lab 5

Created a custom Python module containing an addition function and imported it into a separate script.

**Concepts practiced:**

- Defining functions using `def`
- Importing custom modules
- Handling user input
- Converting strings to numbers
- Retrieving the current date and time

**Verified execution:**

```text
Enter 2 numbers: 10 10
Using the module math_301564663.py : 10.0 + 10.0 = 20.0
Today: 2026-10-16 10:28:24.823710

Process finished with exit code 0
```

**Key takeaway:** Organizing Python functionality into reusable modules instead of keeping everything in one script.

## 2. Python System Administration — Lab 6

Developed a Python script to automate basic Windows filesystem operations.

**Implemented functionality:**

- Check whether directories exist before creating them.
- Create individual and nested directories.
- Retrieve the current working directory and change directories.
- Retrieve the logged-in username and operating system identifier.
- List directory contents.
- Recursively traverse directories using `os.walk()`.
- Calculate the combined size of files within a directory tree.
- Remove an empty temporary directory.

**Core Python methods:**

```python
os.path.exists()
os.mkdir()
os.makedirs()
os.getcwd()
os.chdir()
os.path.join()
os.getlogin()
os.name
os.listdir()
os.walk()
os.path.getsize()
os.rmdir()
```

**Verified results:**

- Target directory structure created successfully.
- Existing directories detected during subsequent execution.
- Directory structure displayed.
- Combined file size reported as `0 bytes` for the empty test directories.
- Temporary student-number directory removed successfully.
- First and second executions completed with exit code `0`.

**Key takeaway:** Filesystem automation requires careful path management, existence checks, loops, and validation to avoid unintended changes.

## 3. Python Networking — Lab 7

Used Python's built-in `socket` module to perform three basic networking operations.

### Hostname resolution

```python
socket.gethostbyname("www.apple.com")
```

**Observed result:**

```text
184.26.202.199
```

DNS results can vary depending on the DNS resolver, network location, and lookup time.

### Network service identification

```python
socket.getservbyport(22)
```

**Result:**

```text
ssh
```

This identifies the registered service associated with port 22. It does not check whether the port is open.

### IPv4 address conversion

```python
socket.inet_aton("192.168.6.17")
```

**Result:**

```text
b'\xc0\xa8\x06\x11'
```

The IPv4 address is represented as four packed bytes, totaling 32 bits.

**Key takeaway:** Python can perform basic networking operations programmatically through its standard library.

## Run the CLI

From the repository root in PowerShell, run:

```powershell
py -3 .\python\04-system-network-admin\main.py
```

Use Python 3.12 or later. The directory inspector uses `os.path.isjunction()` to skip Windows folder redirects during traversal.

## Implemented Features

- Display the computer name, operating system, username, and working directory.
- List directory contents, walk the directory tree, and report the total file size in bytes. The inspector skips symbolic links and junctions when calculating the total. It flags partial results when files or folders cannot be read.
- Resolve a hostname to an IPv4 address and show its four packed bytes.
- Look up the registered service for ports 1–65535 using the operating system's service table.
- Save a timestamped text report in the working directory with the current system details and the latest directory and network results from the session.

`main.py` handles prompts and reports. `system_info.py` handles filesystem and system details. `network_info.py` handles network lookups and IPv4 conversion.

## Verification

Tested on Windows 11 with Python 3.14. All menu options passed, including a nested directory totaling 12 bytes, valid and invalid lookup inputs, and timestamped reports before and after collecting results.

## Planned Improvements

- Let the user choose where to save a report.

## What I Learned

- How Python modules help organize reusable functionality.
- How to automate filesystem operations using the `os` module.
- How nested loops enable recursive directory inspection.
- How the `socket` module interacts with DNS, port-service mappings, and IPv4 representations.
- Why validating paths and handling variable network responses matters in automation.

---

**Course:** CNET 334 — System Scripting
**Institution:** Centennial College
**Focus:** Python, System Administration, Networking & Automation
