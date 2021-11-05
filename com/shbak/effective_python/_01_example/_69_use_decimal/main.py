from decimal import Decimal

from termcolor import colored


def print_cost():
    rate = Decimal('1.45')
    seconds = Decimal(3 * 60 + 42)
    cost = rate * seconds / Decimal(60)
    print(colored(f'cost: {cost}', 'green'))


def compare_str_float():
    print(colored(f'Decimal("1.45"): {Decimal("1.45")}', 'green'))
    print(colored(f'Decimal(1.45): {Decimal(1.45)}', 'green'))


if __name__ == '__main__':
    print_cost()
    compare_str_float()
#     use str instance rather than float
