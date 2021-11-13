# use thread in Blocking I/O(File read/write, Network I/O, Display)
# GIL release, when Blocking I/O and acquire GIL when Blocking I/O is finished
import select
import socket
import time
from threading import Thread

from _distutils_hack import override
from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

class FactorizaeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    # @override
    def run(self):
        self.factor = list(factorize(self.number))
        print(colored(f'self.factor : {self.factor}', 'green'))
        return self.factor

    def join(self):
        Thread.join(self)
        return self.factor

def slow_systemcall():
    # select method's parameter read, write, executable list, and timeout (all empty list is not permitted windows platform)
    select.select([socket.socket()], [], [], 0.1)


@trace_func
def call_slow_systemcall_serial():
    start = time.time()

    for _ in range(5):
        slow_systemcall()
    end = time.time()
    delta = end - start
    print(colored(f'duration : {delta}', 'green'))


@trace_func
def call_slow_systemcall_concurrent():
    start = time.time()
    threads = []
    for _ in range(5):
        # thread = Thread(target=slow_systemcall()) -> if target argument set method() it will slow, and not error occur
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.time()
    delta = end - start
    print(f'Total {delta:.3f} seconds')


def run_factorize_thread(number):
    thread = FactorizaeThread(number)
    result_value = thread.start()
    return thread.join()


if __name__ == '__main__':
    call_slow_systemcall_serial()
    call_slow_systemcall_concurrent()
    return_value = run_factorize_thread(12)
    print(colored(f'return_value: {return_value}', 'green'))
