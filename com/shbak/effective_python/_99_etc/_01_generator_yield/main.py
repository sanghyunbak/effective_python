# iterator implements __iter__, __next__또는__getitem__methods
from termcolor import colored


def generator_method():
    yield 1
    yield "hahaha"
    yield "hihihi"


if __name__ == '__main__':
    it = generator_method()
    print(colored(f'it : {it}', 'green'))
    for i in generator_method():
        print(colored(f'{i}', 'blue'))
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))
    print(colored(f'it.__next__(): {it.__next__()}', 'cyan'))
    print(colored(f'range(3): {range(3)}', 'magenta'))
