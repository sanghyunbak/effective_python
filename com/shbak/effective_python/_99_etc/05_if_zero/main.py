from termcolor import colored


def if_zero():
    if 0:
        print(colored(f'if zero', 'green'))
    else:
        print(colored(f'if zero else', 'green'))


def if_empty_dict():
    if {}:
        print(colored(f'if empty dict', 'green'))
    else:
        print(colored(f'if empty dict else', 'green'))


def if_empty_array():
    if []:
        print(colored(f'if empty array', 'green'))
    else:
        print(colored(f'if empty array else', 'green'))


if __name__ == '__main__':
    if_zero()
    if_empty_array()
    if_empty_dict()
