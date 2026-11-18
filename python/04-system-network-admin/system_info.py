"""Read system details and inspect directories."""

import getpass
import os
import platform


def get_system_info():
    return {
        "Computer": platform.node(),
        "Operating system": platform.platform(),
        "Username": getpass.getuser(),
        "Working directory": os.getcwd(),
    }


def list_directory(path):
    return sorted(os.listdir(path), key=str.casefold)


def walk_directory(path, errors):
    def record_error(error):
        errors.append(str(error))

    for root, directories, files in os.walk(path, onerror=record_error):
        # Keep the walk inside the selected tree, including on Windows.
        directories[:] = sorted(
            (
                name for name in directories
                if not os.path.islink(os.path.join(root, name))
                and not os.path.isjunction(os.path.join(root, name))
            ),
            key=str.casefold,
        )
        yield root, directories, sorted(files, key=str.casefold)


def total_file_size(tree, errors):
    total = 0
    for root, _, files in tree:
        for name in files:
            path = os.path.join(root, name)
            try:
                if not os.path.islink(path):
                    total += os.path.getsize(path)
            except OSError as error:
                errors.append(str(error))
    return total
