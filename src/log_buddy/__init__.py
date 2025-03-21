"""
Logging utilities
"""
from logging import *
import inspect


def modlog():
    """
    Create a logger with a name for the given module
    """
    frame = inspect.stack()[1]
    module_name = inspect.getmodule(frame[0]).__name__
    return getLogger(module_name)
