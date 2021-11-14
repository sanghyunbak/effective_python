from threading import Thread, Lock
from termcolor import colored


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset  # it is not atomic


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # read sensor data
        counter.increment(1)


def thread_counter():
    how_many = 10 ** 5
    print(colored(f'10 ** 5: {how_many}', 'green'))
    counter = Counter()  # critical section

    threads = []
    for i in range(5):
        thread = Thread(target=worker,
                        args=(i, how_many, counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected = how_many * 5
    found = counter.count
    print(colored(f'Counter value expected {expected}, actual {found}', 'green'))


class LockingCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self, offset):
        with self.lock:
            self.count += offset  # it is not atomic


def thread_counter_lock():
    how_many = 10 ** 5
    counter = LockingCounter()  # critical section

    threads = []
    for i in range(5):
        thread = Thread(target=worker,
                        args=(i, how_many, counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected = how_many * 5
    found = counter.count
    print(colored(f'[Locking]Counter value expected {expected}, actual {found}', 'green'))


if __name__ == '__main__':
    thread_counter()
    thread_counter_lock()
