# Project 04 — Python System & Network Administration

## Overview

A Python scripting project developed from practical System Scripting labs at Centennial College.

This project brings together three areas of Python programming:

- **Python Modules:** Creating and importing reusable functions.
- **System Administration:** Managing directories, navigating the filesystem, and retrieving system information.
- **Networking:** Resolving hostnames, identifying network services, and converting IPv4 addresses into packed binary format.

The objective is to consolidate the concepts covered in Labs 5–7 into a more organized Python project focused on system and network administration.

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

## Project Consolidation — Planned

The next step is to refactor the completed lab exercises into a unified command-line utility.

**Planned functionality:**

1. Display system information.
2. Inspect directories and calculate file sizes.
3. Resolve user-provided hostnames.
4. Identify services associated with port numbers.
5. Generate a timestamped text report.

The combined application will use separate Python modules to keep system administration and networking functionality organized.

These features describe the intended project rebuild, not a completed implementation.

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
