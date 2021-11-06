# priority queue
import functools
import random
import timeit
from heapq import heapify, heappop, heappush

from termcolor import colored

from com.shbak.effective_python._01_example._71_dequeue.main import print_results, print_delta


@functools.total_ordering
class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def __lt__(self, other):
        return self.due_date < other.due_date


def add_book(queue, book):
    queue.append(book)
    queue.sort(key=lambda x: x.due_date, reverse=True)


def add_book_heapq(queue, book):
    queue.heappush(book)


def get_queue_from_test_book():
    queue = []
    add_book(queue, Book('Don Quixote', '2019-06-07'))
    add_book(queue, Book('Frankenstein', '2019-06-05'))
    add_book(queue, Book('Les Misérables', '2019-06-08'))
    add_book(queue, Book('War and Peace', '2019-06-03'))
    return queue


def get_ordered_queue_from_test_book():
    queue = []
    add_book(queue, Book('Don Quixote', '2019-06-07'))
    add_book(queue, Book('Frankenstein', '2019-06-05'))
    add_book(queue, Book('Les Misérables', '2019-06-08'))
    add_book(queue, Book('War and Peace', '2019-06-03'))
    heapify(queue)
    return queue


class NoOverDueBooks(Exception):
    pass


def next_overdue_book(queue, now):
    if queue:
        book = queue[-1]
        if book.due_date < now:
            queue.pop()
            return book
    raise NoOverDueBooks


def next_overdue_book_heap(queue, now):
    if queue:
        book = queue[0]
        if book.due_date < now:
            heappop(queue)
            return book
    raise NoOverDueBooks


def test_heap_book_store():
    now = '2019-06-06'
    queue = get_ordered_queue_from_test_book()

    found = next_overdue_book_heap(queue, now)
    print(colored(f'found.title: {found.title}', 'green'))

    found = next_overdue_book_heap(queue, now)
    print(colored(f'found.title: {found.title}', 'green'))

    try:
        next_overdue_book_heap(queue, now)
    except NoOverDueBooks:
        pass
    else:
        assert False


def test_book_store():
    now = '2019-06-10'
    queue = get_queue_from_test_book()

    found = next_overdue_book(queue, now)
    print(colored(f'found.title: {found.title}', 'green'))

    found = next_overdue_book(queue, now)
    print(colored(f'found.title: {found.title}', 'green'))


def list_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            queue.append(i)
            queue.sort(reverse=True)

        while queue:
            queue.pop()

    tests = timeit.repeat(
        setup='queue, to_add = prepare()',
        stmt=f'run(queue, to_add)',
        globals=locals(),
        repeat=100,
        number=1
    )

    return print_results(count, tests)


def list_return_benchmark(count):
    def prepare():
        queue = list(range(count))
        random.shuffle(queue)

        to_return = list(range(count))
        random.shuffle(to_return)

        return queue, to_return

    def run(queue, to_return):
        for i in to_return:
            queue.remove(i)

    tests = timeit.repeat(
        setup='queue, to_return = prepare()',
        stmt=f'run(queue, to_return)',
        globals=locals(),
        repeat=100,
        number=1
    )

    return print_results(count, tests)


def heap_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            heappush(queue, i)
        while queue:
            heappop(queue)

    tests = timeit.repeat(
        setup='queue, to_add = prepare()',
        stmt=f'run(queue, to_add)',
        globals=locals(),
        repeat=100,
        number=1
    )

    return print_results(count, tests)


if __name__ == '__main__':
    test_book_store()
    print(colored(f'list overdue benchmark', 'yellow'))
    baseline = list_overdue_benchmark(500)
    for count in (1_000, 1_500, 2_000):
        comparison = list_overdue_benchmark(count)
        print_delta(baseline, comparison)

    print(colored(f'list return benchmark', 'yellow'))
    baseline = list_return_benchmark(500)
    for count in (1_000, 1_500, 2_000):
        comparison = list_return_benchmark(count)
        print_delta(baseline, comparison)

    print(colored(f'test_heap_book_store', 'yellow'))
    test_heap_book_store()

    print(colored(f'heap overdue benchmark', 'yellow'))
    baseline = heap_overdue_benchmark(500)
    for count in (1_000, 1_500, 2_000):
        comparison = heap_overdue_benchmark(count)
        print_delta(baseline, comparison)
