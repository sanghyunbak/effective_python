import time
from collections import deque
from threading import Lock, Thread
from queue import Queue

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


def download(item):
    print(colored(f'donloading...', 'green'))


def resize(item):
    print(colored(f'resize...', 'green'))


def upload(item):
    print(colored(f'upload...', 'green'))


def thread_run():
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()

    done_queue = MyQueue()

    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue),
    ]

    for thread in threads:
        thread.start()

    for _ in range(1000):
        download_queue.put(object())

    while len(done_queue.items) < 1000:
        pass
    processed = len(done_queue.items)
    polled = sum(t.polled_count for t in threads)
    print(colored(f'{processed} item processed'
                  f'polling {polled} done', 'green'))


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # thread terminate
                yield item
            finally:
                self.task_done()  # Queue method


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


@trace_func
def run_cloasable_queue():
    download_queue = ClosableQueue()
    resize_queue = ClosableQueue()
    upload_queue = ClosableQueue()
    done_queue = ClosableQueue()

    threads = [
        StoppableWorker(download, download_queue, resize_queue),
        StoppableWorker(resize, resize_queue, upload_queue),
        StoppableWorker(upload, upload_queue, done_queue),
    ]

    for thread in threads:
        thread.start()

    for _ in range(1000):
        download_queue.put(object())

    download_queue.close()

    download_queue.join()
    resize_queue.close()
    resize_queue.join()
    upload_queue.close()
    upload_queue.join()

    print(colored(f'done_queue.qsize() : {done_queue.qsize()}'))


def start_threads(count, *args):
    threads = [StoppableWorker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads


def stop_threads(closable_queue, threads):
    for _ in threads:
        closable_queue.close()

    closable_queue.join()

    for thread in threads:
        thread.join()

def call_start_stop_thread():
    download_queue = ClosableQueue()
    resize_queue = ClosableQueue()
    upload_queue = ClosableQueue()
    done_queue = ClosableQueue()

    download_threads = start_threads(3, download, download_queue, resize_queue)
    resize_threads = start_threads(4, resize, resize_queue, upload_queue)
    upload_threads = start_threads(5, upload, upload_queue, done_queue)

    for _ in range(1000):
        download_queue.put(object())

    stop_threads(download_queue, download_threads)
    stop_threads(resize_queue, resize_threads)
    stop_threads(upload_queue, upload_threads)

    print(colored(f'done_queue.qsize(): {done_queue.qsize()} processed'))


if __name__ == '__main__':
    thread_run()
    run_cloasable_queue()
    call_start_stop_thread()