from unittest import TestCase, main

from termcolor import colored


def setUpModule():
    print(colored(f'* module set up', 'green'))


def tearDownModule():
    print(colored(f'* module clean up', 'green'))


class IntegrationTest(TestCase):
    def setUp(self):
        print(colored(f'* Test Setting', 'green'))

    def tearDown(self) -> None:
        print(colored(f'* Test Clean up (tear down)', 'green'))

    def test_end_to_end1(self):
        print(colored(f'* test 1', 'green'))

    def test_end_to_end2(self):
        print(colored(f'* test 2', 'green'))


if __name__ == '__main__':
    main()
