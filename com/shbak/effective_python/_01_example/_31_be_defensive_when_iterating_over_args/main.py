# general scenario: get list argument and iterate
from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


@trace_func
def normalize(numbers):
    count = sum(numbers)
    result = []
    for _, n in enumerate(numbers):
        percent = n / count * 100
        result.append(percent)

    return result


if __name__ == '__main__':
    input = [1, 53, 5]
    print(colored(f'normalize(input): {normalize(input)}', 'green'))
