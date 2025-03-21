"""
Logging function calls and subvalues
"""

from logging import Logger, DEBUG, ERROR
from typing import Callable, Concatenate, ParamSpec, TypeVar
from functools import wraps


__all__ = ["log_function"]


P = ParamSpec("P")
R = TypeVar("R")


def log_function(parent: Logger, level: int = DEBUG, error_level: int = ERROR) -> Callable[[Callable[Concatenate[Logger, P], R]], Callable[P, R]]:
    """
    Decorate a function with code to create sub log context log calls for
    function. The function can also accept it's own log context to provide
    more detailed logs

    NOTE: The function will need to accept a parameter `log` which will
    be the new logger being passed in.

    ```
    @log_function(log)
    def function(log, *args, **kwargs):
        ...
    ```

    :param Logger parent: Logger that the child logger is created from

    :param int level: The level that calls and outputs of the function are logged to

    :param int error_level: If log_error and log_calls is True, this will be
                            the level that error messages are logged in

    :returns logger_decorator: Decorator wraps the provided function
                               with logging utilities
    """

    def logger_wrapper(func: Callable[Concatenate[Logger, P], R]) -> Callable[P, R]:
        """
        Wrap function in logging utilties
        """

        @wraps(func)
        def logged_function(*args: P.args, **kwargs: P.kwargs) -> R:
            """
            Function with wrapped logging functionality
            """
            log = parent.getChild(func.__name__)
            log.log(level, f"Called with args {args} and kwargs {kwargs}")
            try:
                result = func(log, *args, **kwargs)
                log.log(level, f"Returned {result}")
                return result
            except Exception as e:
                log.log(error_level, f"Raised exception: {e!r}")
                raise e

        return logged_function

    return logger_wrapper
