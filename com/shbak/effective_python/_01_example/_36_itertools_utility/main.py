import itertools

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator import trace
from com.shbak.effective_python._01_example._26_decorator.trace import trace_func

_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_acc():
    sum_reduce = itertools.accumulate(_values)
    print(colored(f'sum : {sum_reduce}', 'green'))


def sum_modulo_20(first, second):
    output = first + second
    return output % 20


def sum_sum_modulo_20(first, second):
    output = first + second + first
    return output % 20


@trace.trace_func
def print_acc_modulo_20():
    print(colored(f'_values : {list(_values)}', 'green'))
    modulo_reduce = itertools.accumulate(_values, sum_modulo_20)
    print(colored(f'modulo_reduce: {list(modulo_reduce)}', 'green'))
    sum_sum_modulo_reduce = itertools.accumulate(_values, sum_sum_modulo_20)
    print(colored(f'modulo_reduce: {list(sum_sum_modulo_reduce)}', 'green'))


@trace.trace_func
def itertools_product():
    """ return decart product (cartesian product)

    """
    single = itertools.product([1, 2, ], repeat=2)
    print(colored(f'List one : {list(single)}', 'green'))

    multiple = itertools.product([1, 2], ['a', 'b'])
    print(colored(f'List Two: {list(multiple)}', 'green'))


def print_permutation():
    pass


# permutation is ordered combination
def print_permuation():
    # itertools.permutations returns a length N permutation('N' refers to second argument)
    it = itertools.permutations([1, 2, 3, 4], 2)
    print(colored(f'permutation result of arg : [1, 2, 3 ,4], 2 -> {list(it)}', 'green'))


@trace_func
def print_combination():
    # itertools.permutations returns a length N permutation('N' refers to second argument)
    it = itertools.combinations([1, 2, 3, 4], 2)
    print(colored(f'combination result of arg : [1, 2, 3 ,4], 2 -> {list(it)}', 'green'))


@trace_func
def print_combination_with_replacement():
    """ combination with same element

    """
    it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
    print(colored(f'combination result of arg : [1, 2, 3 ,4], 2 -> {list(it)}', 'green'))


if __name__ == '__main__':
    print_acc()
    print_acc_modulo_20()
    itertools_product()
    print_permutation()
    print_combination()
    print_combination_with_replacement()
