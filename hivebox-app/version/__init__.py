import subprocess
import os

def get_version():
    try:
        try:
            version = subprocess.check_output(
                ["git", "describe", "--tags", "--always"],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
            return version
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
        return os.getenv("APP_VERSION", "unknown")
    except Exception:
        version = "unknown"
    return version

__version__ = get_version()