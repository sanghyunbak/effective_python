from functools import wraps
import concurrent.futures
import time

from termcolor import colored


def test_func(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("start...")
        res = func(*args, **kwargs)
        print("end...")
        return res

    return inner


@test_func
def test1():
    print('run test1 ....')
    time.sleep(10)

    return 1


@test_func
def test2():
    print('run test2 ....')
    time.sleep(10)

    return 1


@test_func
def test3():
    print('run test3 ....')
    time.sleep(10)

    return 1


@test_func
def test4():
    print('run test4 ....')
    time.sleep(10)

    return 1


def main():
    funcs = [test1, test2, test3, test4]

    executor = concurrent.futures.ThreadPoolExecutor(4)
    futures = []
    # while True:
    for func in funcs:
        futures.append(executor.submit(func))
        time.sleep(5)
        print(colored(f'qsize: {executor._work_queue.qsize()}', 'green'))
        print(colored(f'qsize: {concurrent.futures.ThreadPoolExecutor.__itemsize__}', 'green'))

    for future in futures:
        future.result()


if __name__ == '__main__':
    main()
