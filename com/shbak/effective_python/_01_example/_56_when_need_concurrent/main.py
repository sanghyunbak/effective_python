# author: Conway
# game title: Game of life
# rule: 5 x 5 grid consist of cell, cell status is EMPTY or ALIVE
#       when ticks pass around 8 cell's status make cell's ALIABILITY (the number of ALIVE cell)
import select
import socket

from termcolor import colored

ALIVE = '*'
EMPTY = '-'


class Grid:
    def __init__(self, height, width):
        """initial setting all cells are EMPTY

        :param height:
        :param width:
        """
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, x, y):
        return self.rows[y % self.height][x % self.width]

    # why % operation?
    # requirements of client (wrap around)
    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        result = ''
        for y in range(self.height):
            for x in range(self.width):
                result += self.rows[y][x]
            result += '\n'
        return result


def count_neighbors(x, y, get):
    n_ = get(y - 1, x + 0)
    ne = get(y - 1, x + 1)
    e_ = get(y + 0, x + 1)
    se = get(y + 1, x + 1)
    s_ = get(y + 1, x + 0)
    sw = get(y + 1, x - 1)
    w_ = get(y + 0, x - 1)
    nw = get(y - 1, x - 1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def game_logic(state, neighbors):
    select.select([socket.socket()], [], [], 0.1)
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors < 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)


def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y, x, grid.get, next_grid.set)   # functional interface
    return next_grid


def grid_setting():
    grid = Grid(5, 9)
    grid.set(0, 3, ALIVE)
    grid.set(1, 4, ALIVE)
    grid.set(2, 2, ALIVE)
    grid.set(2, 3, ALIVE)
    print(colored(f'{grid}', 'green'))

if __name__ == '__main__':
    grid_setting()
    pass
