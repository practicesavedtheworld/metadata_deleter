import functools
from typing import Callable, ParamSpec, TypeVar

from src.tools.print_colorful import print_colorful

T = TypeVar("T")
P = ParamSpec("P")


def notify(operation: str) -> Callable[[Callable[P, T]], Callable[P, T | None]]:
    """Based on |operation| parameter tells what exactly executed or failed"""

    def notifier(func: Callable[P, T]) -> Callable[P, T | None]:
        """Notifies user that something completed or went wrong"""

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T | None:
            func_exc_result = None
            try:
                func_exc_result = func(*args, **kwargs)
                print_colorful(f"{operation} executed successfully", "green")
            except Exception as err:
                # TODO log that
                print_colorful(f"{operation} execution failed", "red")
            finally:
                return func_exc_result

        return wrapper

    return notifier
