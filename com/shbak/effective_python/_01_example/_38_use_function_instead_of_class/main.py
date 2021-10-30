# hook : function that pass to parameter and do some objective role
from collections import defaultdict

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func

_current = {'green': 12, 'blue': 3}
_increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

def log_missing():
    print(colored(f'key added', 'green'))
    return 0


@trace_func
def print_defaultdict():
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9)
    ]
    result = defaultdict(log_missing, current)
    print(colored(f'Before: {dict(result)}', 'green'))
    for key, amount in increments:
        result[key] += amount
    print(colored(f'After: {dict(result)}', 'green'))


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


@trace_func
def use_count_missing_class():
    counter = CountMissing()
    result = defaultdict(counter.missing, _current)
    for key, amount in _increments:
        result[key] += amount

    print(colored(f'counter.added : {counter.added}', 'green'))


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


@trace_func
def use_count_better_count_missing():
    counter = BetterCountMissing()
    result = defaultdict(counter, _current)
    for key, amount in _increments:
        result[key] += amount
    print(colored(f'counter.added: {counter.added}', 'green'))


if __name__ == '__main__':
    print_defaultdict()
    use_count_missing_class()
    use_count_better_count_missing()
