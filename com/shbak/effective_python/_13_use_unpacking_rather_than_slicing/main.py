#
from termcolor import colored


car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)


# oldest, second_oldest = car_ages_descending
# use starred(*) expression
# expression and statement relation is statement contain expression
# expression is return a value
def asterisk_unpacking_for_unknown_the_number_of_elements():
    print(colored(f'method: {asterisk_unpacking_for_unknown_the_number_of_elements.__name__}() called', 'yellow'))
    oldest, second_oldest, *others = car_ages_descending
    # *others = car_ages_descending
    print(colored(f'oldest : {oldest}', 'green'))
    print(colored(f'oldest : {second_oldest}', 'green'))
    print(colored(f'others : {others}', 'green'))



def print_unpacking_empty_list():
    print(colored(f'method: {print_unpacking_empty_list.__name__}() called'), 'yellow')
    short_list = [1, 2]
    first, second, *rest = short_list
    print(colored(f'code print \n{print_unpacking_empty_list.__code__}'
                  f'\nprint_unpacking_empty_list.__dir__():z{print_unpacking_empty_list.__dir__()}', 'blue'))
    print(colored(f'first, second, *rest = short_list', 'green'))
    print(colored(f'first: {first}', 'green'))
    print(colored(f'second: {second}', 'green'))
    print(colored(f'rest: {rest}', 'green'))


if __name__ == '__main__':
    asterisk_unpacking_for_unknown_the_number_of_elements()
    print_unpacking_empty_list()
