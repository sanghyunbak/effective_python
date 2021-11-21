import timeit

from termcolor import colored

G_VAR = 1
G_VAR2 = 2

def global_test():
    return 1

def benchmark_globals():
    def sum_test():
        return G_VAR + 3

    result = timeit.timeit(
        setup='G_VAR2',
        stmt='global_test()',
        globals=globals(),
        number=3
    )

    # locals = locals()

    # dir(locals)

    print(colored(f'{result} sec', 'green'))


if __name__ == '__main__':
    benchmark_globals()