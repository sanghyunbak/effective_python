# use collections abc because direct implementation of container cause error

import traceback
from collections.abc import Sequence

from termcolor import colored


class BadType(Sequence):
    pass


def create_badtype_object():
    try:
        foo = BadType()
    except TypeError as e:
        print(colored(f'Type error occur', 'yellow'))
        print(colored(f'{e}', 'red'))
        traceback.print_exc()


if __name__ == '__main__':
    create_badtype_object()
    print(colored(f'hihihi', 'green'))
