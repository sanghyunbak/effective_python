# Object's private attribute is naming change from <private attribute name> to _<object name><private attribute name>
from termcolor import colored

class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field



def call_private_value():
    foo = MyObject()
    try:
        print(colored(f'foo.__private_field: {foo.__private_field}', 'green'))
    except AttributeError:
        print(colored(f'No attribute error occur', 'red'))


def call_private_value_other_name():
    foo = MyObject()
    dict_value = foo.__dict__
    print(colored(f'dict_value : {dict_value}', 'green'))
    value = foo._MyObject__private_field # not show in IDE auto complete
    print(colored(f'value : {value}', 'green'))


if __name__ == '__main__':
    call_private_value()
    call_private_value_other_name()