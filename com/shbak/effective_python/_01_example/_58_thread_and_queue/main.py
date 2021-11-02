from queue import Queue
from termcolor import colored

from com.shbak.effective_python._01_example._55_queue_for_thread.main import ClosableQueue, StoppableWorker
from com.shbak.effective_python._01_example._56_when_need_concurrent.main import game_logic, count_neighbors, Grid, \
    ALIVE


def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)


class ColumnPrinter():
    deilmeter = '|\n'
    def __init__(self):
        self.list = list()

    def __call__(self):
        return self.list

    def __str__(self):
        return '---'

def thread_and_queue_test():
    in_queue = ClosableQueue()
    out_queue = ClosableQueue()

    threads = []
    for _ in range(5):
        thread = StoppableWorker(game_logic_thread, in_queue, out_queue)
        thread.start()
        threads.append(thread)

    grid = Grid(5, 9)
    grid.set(0, 3, ALIVE)
    grid.set(1, 4, ALIVE)
    grid.set(2, 2, ALIVE)
    grid.set(2, 3, ALIVE)
    grid.set(2, 4, ALIVE)

    columns = []
    for i in range(5):
        columns.append(str(grid))
        grid = simulate_pipeline(grid, in_queue, out_queue)

    print(colored(f'{columns}', 'green'))

    for thread in threads:
        in_queue.close()
    for thread in threads:
        thread.join()

class SimulationError(Exception):
    pass


def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))  # fan out

    in_queue.join()
    out_queue.close()

    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)

    return next_grid


if __name__ == '__main__':
    thread_and_queue_test()
    pass
