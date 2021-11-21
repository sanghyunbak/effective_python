from termcolor import colored


def func_print():
    a = 3
    # print(colored(f'aa %s',% a, 'green'))
    print('%s %s' % (a, a))


if __name__ == '__main__':
    func_print()
