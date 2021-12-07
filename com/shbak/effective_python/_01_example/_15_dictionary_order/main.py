from termcolor import colored

_baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}

if __name__ == '__main__':
    print(colored(f'_baby_names: {_baby_names}', 'green'))
    print(colored(f'============== Return Lists ============', 'magenta'))
    print(colored(f'_baby_names.keys(): {_baby_names.keys()}', 'green'))
    print(colored(f'_baby_names.values(): {_baby_names.values()}', 'green'))
    print(colored(f'_baby_names.items(): {_baby_names.items()}', 'green'))
