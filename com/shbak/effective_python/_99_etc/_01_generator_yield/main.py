# iterator implements __iter__, __next__또는__getitem__methods
# iterator can't copy
# iterator can't reverse (one-way)
from termcolor import colored


def generator_method():
    yield 1
    yield "hahaha"
    yield "hihihi"


_it = generator_method()


# can't copy generator
def iterate_with_next_method():
    print(colored(f'method: {iterate_with_next_method.__name__}', 'yellow'))
    # it = copy.deepcopy(_it)
    # it = itertools.tee(_it)
    it = generator_method()
    print(colored(f'next(it): {next(it)}', 'cyan'))
    print(colored(f'next(it): {next(it)}', 'cyan'))
    print(colored(f'next(it): {next(it)}', 'cyan'))


def iterate_with___next__():
    print(colored(f'method: {iterate_with___next__.__name__}()', 'yellow'))
    # it = itertools.tee(_it)
    # it = copy.deepcopy(_it)
    it = generator_method()
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))


if __name__ == '__main__':
    print(colored(f'it : {_it}', 'green'))
    for i in generator_method():
        print(colored(f'{i}', 'blue'))
    iterate_with_next_method()
    iterate_with___next__()
