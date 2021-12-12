from termcolor import colored

_baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}


def my_func(**kwargs):
    print(colored(f'type(kwargs): {type(kwargs)}', 'green'))
    for key, value in kwargs.items():
        print('%s = %s' % (key, value))


if __name__ == '__main__':
    print(colored(f'_baby_names: {_baby_names}', 'green'))
    print(colored(f'_baby_names.keys(): {_baby_names.keys()}', 'green'))
    print(colored(f'type(_baby_names.keys()): {type(_baby_names.keys())}', 'green'))
    print(colored(f'_baby_names.values(): {_baby_names.values()}', 'green'))
    print(colored(f'_baby_names.items(): {_baby_names.items()}', 'green'))
    print(colored(f'_baby_names.items(): {list(_baby_names.items())}', 'green'))
    my_func(a='a', b='b')