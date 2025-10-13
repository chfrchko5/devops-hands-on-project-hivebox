from importlib.metadata import version
__version__ = version("hivebox-app")

def print_version():
    return __version__