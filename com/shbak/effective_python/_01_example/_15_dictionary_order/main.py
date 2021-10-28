from termcolor import colored

_baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}

if __name__ == '__main__':
    print(colored(f'_baby_names: {_baby_names}', 'green'))
