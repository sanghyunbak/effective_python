from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


@trace_func
def print_str():
    my_value = 'foo bar'
    print(str(my_value))
    print('%s' % my_value)
    print(f'{my_value}')
    print(format(my_value))
    print(my_value.__format__('s'))
    print(my_value.__str__())


@trace_func
def print_repr():
    a = '\x07'
    print(colored(f'repr(a): {repr(a)}', 'green'))
    print(colored(f'a: {a}', 'green'))

    # repr and eval of repr is same
    b = eval(repr(a))
    print(colored(f'b = repr(a)', 'magenta'))
    print(colored(f'a == b: {a == b}', 'green'))
    # % operator
    print(colored(f'%r' % 5, 'green'))
    print(colored(f'{{b!r}}: {b!r}', 'green'))


class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def print_opaque():
    obj = OpaqueClass(1, 'foo')
    print(colored(f'OpaqueClass obj: {obj}', 'green'))


class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'


def print_better_class():
    obj = BetterClass(2, 'bar')
    print(colored(f'BetterClass obj: {obj}', 'green'))


@trace_func
def show_str_int():
    int_var = 5
    str_var = '5'

    print(colored(f'repr statements distinguish string and integer', 'yellow'))
    print(colored(f'int_var: {int_var!r}\nstr_var: {str_var!r}', 'green'))



if __name__ == '__main__':
    show_str_int()
    print_str()
    print_repr()
    print_opaque()
    print_better_class()
