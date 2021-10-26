from termcolor import colored

from com.shbak.effective_python._01_example._14_sort.tool import Tool

_tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('끌', 0.25),
]


if __name__ == '__main__':
    _tools.sort(key=lambda x: x.name)
    print(colored(f'sorted _tools: {_tools}', 'green'))
    result = map(lambda x: x+10, [1, 2, 3])
    for i in result:
        print(colored(f'result: {i}', 'green'))
