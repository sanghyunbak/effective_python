from termcolor import colored


def sort_priority_use_nonlocal(numbers, group):
    """ add nonlocal keyword to assign outter value

    :param numbers:
    :param group:
    :return:
    """
    found = False

    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found # outer function variable "found" not reference inner function


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        if x in group:
            # found = found
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found # outer function variable "found" not reference inner function


def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found # outer function variable "found" not reference inner function


def sort_priority(values, group):
    """

    :param values:
    :param group:
    :return:
    """
    def helper(x):
        if x in group:
            return 0, x
        return 1, x
    values.sort(key=helper)


def call_sort_priority():
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 8, 7}
    a = {1:2, 3:5}

    print(colored(f'numbers: {numbers}', 'green'))
    print(colored(f'group: {group}', 'green'))
    print(colored(f'a: {a}', 'green'))
    print(colored(f'isinstance(group, dict): {isinstance(group, dict)}', 'magenta'))
    print(colored(f'isinstance(group, set): {isinstance(group, set)}', 'magenta'))
    print(colored(f'isinstance(a, dict): {isinstance(a, dict)}', 'magenta'))
    sort_priority(numbers, group)
    print(colored(f'[Sorted]numbers: {numbers}', 'green'))


if __name__=='__main__':
    call_sort_priority()