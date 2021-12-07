from com.shbak.effective_python._01_example._14_sort.tool import Tool
from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func

_tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('끌', 0.25),
]


@trace_func
def sort_with_priority():
    saw = (5, '원형톱')
    jackhammer = (40, '착암기')
    assert not (jackhammer < saw)


@trace_func
def sort_with_tuple():
    print(colored(f'method: {sort_with_tuple.__name__}() called', 'yellow'))
    _tools.sort(key=lambda x: (x.weight, x.name))
    print(colored(f'sorted with tuple: {_tools}', 'green'))


@trace_func
def sort_with_tuple_with_reverse_order_some_tuple_element():
    print(colored(f'method: {sort_with_tuple_with_reverse_order_some_tuple_element.__name__}() called', 'yellow'))
    _tools.sort(key=lambda x: (-x.weight, x.name))
    print(colored(f'sorted with tuple: {_tools}', 'green'))


@trace_func
def sort_with_tuple_with_reverse_order():
    print(colored(f'method: {sort_with_tuple_with_reverse_order_some_tuple_element.__name__}() called', 'yellow'))
    _tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
    print(colored(f'sorted with tuple: {_tools}', 'green'))


if __name__ == '__main__':
    # _tools.sort()
    _tools.sort(key=lambda x: x.name)
    print(colored(f'\nSorted: {_tools}', 'green'))
    sort_with_priority()
    sort_with_tuple()
    sort_with_tuple_with_reverse_order_some_tuple_element()
    sort_with_tuple_with_reverse_order()