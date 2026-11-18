"""Run the system and network administration menu."""

import os
from datetime import datetime
from pathlib import Path

from network_info import lookup_service, pack_ipv4, resolve_hostname
from system_info import get_system_info, list_directory, total_file_size, walk_directory


MENU = """
1. Display system information
2. Inspect a directory and calculate its total file size
3. Resolve a hostname to an IPv4 address
4. Identify the service associated with a port
5. Generate a timestamped text report
0. Exit
"""


def format_system_info():
    return "\n".join(f"{label}: {value}" for label, value in get_system_info().items())


def inspect_directory():
    entered_path = input("Directory path: ").strip().strip('"')
    if not entered_path:
        raise ValueError("Enter a directory path.")
    path = os.path.abspath(os.path.expanduser(entered_path))
    contents = list_directory(path)
    print("Immediate contents:", ", ".join(contents) or "(empty)")

    errors = []
    tree = []
    print("Directory tree:")
    for root, directories, files in walk_directory(path, errors):
        tree.append((root, directories, files))
        print(f"  {os.path.relpath(root, path)}")
        for name in files:
            print(f"    {name}")

    size = total_file_size(tree, errors)
    summary = f"{path}\nTotal file size: {size} bytes"
    if errors:
        summary += f" (partial, {len(errors)} error(s))"
        for error in errors:
            print(f"Warning: {error}")
    print(summary)
    return summary


def write_report(results):
    now = datetime.now()
    path = Path.cwd() / f"system-network-report-{now:%Y%m%d-%H%M%S-%f}.txt"
    sections = [
        "System and Network Administration Report",
        f"Generated: {now:%Y-%m-%d %H:%M:%S} (local time)",
        f"System information\n{format_system_info()}",
    ]
    for label, result in results.items():
        sections.append(f"{label}\n{result}")

    # Exclusive creation preserves any existing report with the same name.
    with path.open("x", encoding="utf-8") as report:
        report.write("\n\n".join(sections) + "\n")
    return path


def main():
    results = dict.fromkeys(("Directory inspection", "Hostname lookup", "Port lookup"), "Not collected yet.")

    while True:
        try:
            print(MENU)
            choice = input("Choose an option: ").strip()
            if choice == "0":
                print("Goodbye.")
                break
            if choice == "1":
                print(format_system_info())
            elif choice == "2":
                results["Directory inspection"] = inspect_directory()
            elif choice == "3":
                hostname = input("Hostname: ").strip()
                address = resolve_hostname(hostname)
                result = f"{hostname} -> {address}\nPacked IPv4 bytes: {pack_ipv4(address)!r}"
                print(result)
                results["Hostname lookup"] = result
            elif choice == "4":
                port = input("Port number: ").strip()
                service = lookup_service(port)
                result = f"Port {int(port)}: {service}"
                print(result)
                results["Port lookup"] = result
            elif choice == "5":
                print(f"Report saved to {write_report(results)}")
            else:
                print("Choose a number from 0 to 5.")
        except (OSError, ValueError) as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()
