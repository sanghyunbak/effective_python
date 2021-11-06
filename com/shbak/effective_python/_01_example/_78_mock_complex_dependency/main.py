# https://github.com/bslatkin/effectivepython/blob/master/example_code/item_78.py

from datetime import datetime
from unittest.mock import Mock

from termcolor import colored


class DatabaseConnection:
    def __init__(self, ip='localhost', port='5432', account={'user': 'admin', 'pw': 'admin'}):
        print(colored(f'this is database connection class constuctor', 'green'))
        self.ip = ip
        self.port = port
        self.account = account


def get_animals(database, species):
    # connect to database
    #  query species
    animal = 'dog'
    date = datetime(2019, 6, 5, 11, 15)
    return animal, date


_mock = Mock(spec=get_animals)
_expected = [
    ('Spot', datetime(2019, 6, 5, 11, 15)),
    ('Fluffy', datetime(2019, 6, 5, 12, 30)),
    ('Jojo', datetime(2019, 6, 5, 12, 45)),
]

# mock return_value that value when call mock function
_mock.return_value = _expected


class MyError(Exception):
    pass


_mock.side_effect = MyError('Whoops! Big problem')
from datetime import datetime
from unittest.mock import Mock

from termcolor import colored


class DatabaseConnection:
    def __init__(self, ip='localhost', port='5432', account={'user': 'admin', 'pw': 'admin'}):
        print(colored(f'this is database connection class constuctor', 'green'))
        self.ip = ip
        self.port = port
        self.account = account


def get_animals(database, species):
    # connect to database
    #  query species
    animal = 'dog'
    date = datetime(2019, 6, 5, 11, 15)
    return animal, date


_mock = Mock(spec=get_animals)
_expected = [
    ('Spot', datetime(2019, 6, 5, 11, 15)),
    ('Fluffy', datetime(2019, 6, 5, 12, 30)),
    ('Jojo', datetime(2019, 6, 5, 12, 45)),
]

# mock return_value that value when call mock function
_mock.return_value = _expected


class MyError(Exception):
    pass


_mock.side_effect = MyError('Whoops! Big problem')


if __name__ == '__main__':
    database = DatabaseConnection()
    result = get_animals(database, 'Meerkat')
    print(colored(f'result: {result!r}', 'green'))
    result = _mock(database, 'Meerkat')
    _mock.assert_called_once_with(database, 'Meerkat')
    print(colored(f'result: {result}', 'green'))
    _mock('Meerkat')
