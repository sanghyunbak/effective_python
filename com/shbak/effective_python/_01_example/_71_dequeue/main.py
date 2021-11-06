# publish-subscribe queue
import collections
import timeit

from termcolor import colored


class Email:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message


class NoEmailError(Exception):
    pass


def try_receive_email():
    # return email instance or raise except
    pass


def produce_email(queue):
    while True:
        try:
            email = try_receive_email()
        except NoEmailError:
            return
        else:
            queue.append(email)  # producer


def consume_one_email(queue):
    if not queue:
        return
    # email = queue.pop(0)  # consumer
    email = queue.popleft(0)  # consumer


def loop(queue, keep_running):
    while keep_running():
        produce_email(queue)
        consume_one_email(queue)


def my_end_func():
    pass


def print_results(count, tests):
    avg_iteration = sum(tests) / len(tests)
    print(colored(f'# of elements: {count:>5,} Time elapse: {avg_iteration:.6f} sec', 'green'))
    return count, avg_iteration


def list_append_benchmark(count):
    def run(queue):
        for i in range(count):
            queue.append(i)

    tests = timeit.repeat(
        setup='queue= []',
        stmt='run(queue)',
        globals=locals(),
        repeat=1000,
        number=1
    )

    return print_results(count, tests)


def print_delta(before, after):
    before_count, before_time = before
    after_count, after_time = after
    growth = 1 + (after_count - before_count) / before_count
    slowdown = 1 + (after_time - before_time) / before_time
    print(colored(f'Data size: {growth:>4.1f}x, elapse: {slowdown:>4.1f}x speed'))


def list_pop_benchmark(count):
    def prepare():
        return list(range(count))

    def run(queue):
        while queue:
            queue.pop(0)

    tests = timeit.repeat(
        setup='queue = prepare()',
        stmt='run(queue)',
        globals=locals(),
        repeat=1000,
        number=1
    )

    return print_results(count, tests)


def deque_append_benchmark(count):
    def prepare():
        return collections.deque()

    def run(queue):
        for i in range(count):
            queue.append(i)

    tests = timeit.repeat(
        setup='queue = prepare()',
        stmt='run(queue)',
        globals=locals(),
        repeat=1000,
        number=1
    )

    return print_results(count, tests)


def dequeue_popleft_benchmark(count):
    def prepare():
        return collections.deque(range(count))

    def run(queue):
        while queue:
            queue.popleft()

    tests = timeit.repeat(
        setup='queue = prepare()',
        stmt='run(queue)',
        globals=locals(),
        repeat=1000,
        number=1
    )

    return print_results(count, tests)


if __name__ == '__main__':
    loop(collections.deque(), my_end_func)
    baseline = list_append_benchmark(500)
    for count in (1_000, 2_000, 3_000, 4_000, 5_000):
        comparison = list_append_benchmark(count)
        print_delta(baseline, comparison)

    baseline = list_pop_benchmark(500)

    for count in (1_000, 2_000, 3_000, 4_000, 5_000):
        comparison = list_pop_benchmark(count)
        print_delta(baseline, comparison)

    baseline = deque_append_benchmark(500)
    for count in (1_000, 2_000, 3_000, 4_000, 5_000):
        comparision = deque_append_benchmark(count)
        print_delta(baseline, comparision)

    baseline = dequeue_popleft_benchmark(500)

    for count in (1_000, 2_000, 3_000, 4_000, 5_000):
        comparision = dequeue_popleft_benchmark(count)
        print_delta(baseline, comparision)
