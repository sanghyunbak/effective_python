import random
import timeit
from bisect import bisect_left

from termcolor import colored

data = list(range(10 ** 5))
index = data.index(91234)
assert index == 91234


def find_closest(sequence, goal):
    for index, value in enumerate(sequence):
        if goal < value:
            return index
    raise ValueError(f'Over range: {goal}')


_size = 10 ** 5
_iterations = 1000
_data = list(range(_size))
to_lookup = [random.randint(0, _size) for _ in range(_iterations)]


def run_linear(data, to_lookup):
    for index in to_lookup:
        data.index(index)


def run_bisect(data, to_lookup):
    for index in to_lookup:
        bisect_left(data, index)


if __name__ == '__main__':
    index = find_closest(data, 91234.56)
    print(colored(f'[find_closest]: {index}', 'green'))
    assert index == 91235

    index = bisect_left(data, 91234)
    print(colored(f'[bisect, 91234]: {index}', 'green'))
    assert index == 91234

    index = bisect_left(data, 91234.56)
    print(colored(f'[bisect, 91234.56]{index}', 'green'))
    assert index == 91235

    index = bisect_left(data, 91234.23)
    print(colored(f'[bisect, 91234.23]{index}', 'green'))
    assert index == 91235

    baseline = timeit.timeit(
        stmt='run_linear(data, to_lookup)',
        globals=globals(),
        number=10
    )

    print(colored(f'[linear search]: {baseline:.6f} sec', 'green'))

    comparison = timeit.timeit(
        stmt='run_bisect(data, to_lookup)',
        globals=globals(),
        number=10
    )

    print(colored(f'[binary search]: {comparison:.6f} sec', 'magenta'))

    slowdown = 1 + ((baseline - comparison) / comparison)
    print(colored(f'linear search is {slowdown:.1f}x longer'))
