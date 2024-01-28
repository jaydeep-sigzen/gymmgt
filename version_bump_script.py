# version_bump_script.py

import re

def get_current_version():
    with open("./gymmgt/__init__.py", "r") as f:
        content = f.read()
        match = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content)
        if match:
            return match.group(1)
    return None

def update_version(new_version):
    with open("./gymmgt/__init__.py", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("__version__"):
            lines[i] = f'__version__ = "{new_version}"\n'

    with open("./gymmgt/__init__.py", "w") as f:
        f.writelines(lines)

def bump_version(version, part):
    major, minor, patch = map(int, version.split("."))
    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid version part. Use 'major', 'minor', or 'patch'.")

    new_version = f"{major}.{minor}.{patch}"
    return new_version

current_version = get_current_version()
if current_version is not None:
    print(f"Current version: {current_version}")

    # Example: Bump minor version
    new_version = bump_version(current_version, "minor")
    print(f"Bumping to new version: {new_version}")

    # Update the version in __init__.py
    update_version(new_version)
    print("Version updated successfully!")
else:
    print("Unable to retrieve the current version from __init__.py.")
