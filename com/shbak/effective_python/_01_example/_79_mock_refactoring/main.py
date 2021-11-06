import contextlib
import io
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from termcolor import colored


class ZooDatabase:

    def get_animals(self, species):
        pass

    def get_food_period(self, species):
        pass

    def feed_animal(self, name, when):
        pass


def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = database.get_food_period(species)
    animals = database.get_animals(species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) >= feeding_timedelta:
            database.feed_animal(name, now)
            fed += 1

    return fed


DATABASE = None


def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase()
    return DATABASE


def main(argv):
    database = get_database()
    species = argv[1]
    count = do_rounds(database, species)
    print(colored(f'Fed {count} {species}(s)', 'green'))
    return 0


def patch_mock():
    with patch('__main__.DATABASE', spec=ZooDatabase):
        now = datetime.utcnow()

        DATABASE.get_food_period.return_value = timedelta(hours=3)
        DATABASE.get_animals.return_value = [
            ('Spot', datetime(2019, 6, 5, 11, 15)),
            ('Fluffy', datetime(2019, 6, 5, 12, 30)),
            ('Jojo', datetime(2019, 6, 5, 12, 55))
        ]

        fake_stdout = io.StringIO()
        with contextlib.redirect_stdout(fake_stdout):
            main(['program name', 'Meerkat'])

        found = fake_stdout.getvalue()
        expected = 'Fed 2 Meerkat(s)\n'
        print(colored(f'found: {found}', 'green'))
        print(colored(f'expected: {expected}', 'green'))
        assert found == expected


if __name__ == '__main__':
    # database = Mock(spec=ZooDatabase)
    # print(database.feed_animal)
    # database.feed_animal()
    # database.feed_animal.assert_any_call()
    patch_mock()
