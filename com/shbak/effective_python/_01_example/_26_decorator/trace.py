#
from functools import wraps

from termcolor import colored


def trace_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(colored(f'method: {func.__name__}() called', 'yellow'))
        return func(*args, **kwargs)
    return wrapper
