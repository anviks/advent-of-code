import re

from utils_anviks import Cell, Grid, stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = re.findall(r'^(.+) (\d+),(\d+) through (\d+),(\d+)$', f.read(), re.MULTILINE)
data = [(cmd, int(ax), int(ay), int(bx), int(by)) for cmd, ax, ay, bx, by in data]
grid = Grid.fill(1000, 1000, 0)


@stopwatch
def part1():
    for cmd, ax, ay, bx, by in data:
        if cmd == 'turn on':
            grid[Cell(ax, ay):Cell(bx, by)] = 1
        elif cmd == 'turn off':
            grid[Cell(ax, ay):Cell(bx, by)] = 0
        else:
            assert cmd == 'toggle'
            on = [c for c in grid.find(1) if ax <= c.row <= bx and ay <= c.column <= by]
            off = [c for c in grid.find(0) if ax <= c.row <= bx and ay <= c.column <= by]
            if on:
                grid[on] = 0
            if off:
                grid[off] = 1
    return len(list(grid.find(1)))


@stopwatch
def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 569999    | 30 seconds
    print(part2())
