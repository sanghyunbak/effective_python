#
from termcolor import colored


car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

# oldest, second_oldest = car_ages_descending
def asterisk_unpacking_for_unknown_the_number_of_elements():
    print(colored(f'method: {asterisk_unpacking_for_unknown_the_number_of_elements.__name__}() called', 'yellow'))
    oldest, second_oldest, *others = car_ages_descending
    print(colored(f'oldest : {oldest}', 'green'))
    print(colored(f'oldest : {second_oldest}', 'green'))
    print(colored(f'others : {others}', 'green'))


if __name__ == '__main__':
    asterisk_unpacking_for_unknown_the_number_of_elements()