import subprocess

def get_version():
    try:
        version = subprocess.check_output(
            ["git", "describe", "--tags", "--always"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        version = "unknown"
    return version
