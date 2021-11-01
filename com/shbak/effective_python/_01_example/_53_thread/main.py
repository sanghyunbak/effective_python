# use thread in Blocking I/O
import select
import socket
import time
from threading import Thread

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


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


if __name__ == '__main__':
    call_slow_systemcall_serial()
    call_slow_systemcall_concurrent()
