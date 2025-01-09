import re

import numpy as np
from utils_anviks import stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = re.findall(r'^(.+) (\d+),(\d+) through (\d+),(\d+)$', f.read(), re.MULTILINE)
data = [(cmd, int(ax), int(ay), int(bx), int(by)) for cmd, ax, ay, bx, by in data]


@stopwatch
def part1():
    grid = np.zeros((1000, 1000), dtype=int)

    for cmd, ax, ay, bx, by in data:
        if cmd == 'turn on':
            grid[ax:bx + 1, ay:by + 1] = 1
        elif cmd == 'turn off':
            grid[ax:bx + 1, ay:by + 1] = 0
        else:  # 'toggle'
            grid[ax:bx + 1, ay:by + 1] ^= 1

    return grid.sum()


@stopwatch
def part2():
    grid = np.zeros((1000, 1000), dtype=int)

    for cmd, ax, ay, bx, by in data:
        if cmd == 'turn on':
            grid[ax:bx + 1, ay:by + 1] += 1
        elif cmd == 'turn off':
            grid[ax:bx + 1, ay:by + 1] = np.maximum(0, grid[ax:bx + 1, ay:by + 1] - 1)
        else:  # 'toggle'
            grid[ax:bx + 1, ay:by + 1] += 2

    return grid.sum()


if __name__ == '__main__':
    print(part1())  # 569999    | 0.027 seconds
    print(part2())  # 17836115  | 0.076 seconds
