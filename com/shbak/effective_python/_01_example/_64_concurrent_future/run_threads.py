import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from com.shbak.effective_python._01_example._64_concurrent_future import my_module

NUMBERS = [
    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]


def main_threadpool():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=2)
    # pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(my_module.gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'ThreadPool Total {delta:.3f} sec')


def main_processpool():
    start = time.time()
    # pool = ThreadPoolExecutor(max_workers=2)
    pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(my_module.gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'ProcessPool Total {delta:.3f} sec')


if __name__ == '__main__':
    main_threadpool()
    main_processpool()
