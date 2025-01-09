import re

from utils_anviks import stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = re.findall(r'^(.+) (\d+),(\d+) through (\d+),(\d+)$', f.read(), re.MULTILINE)
data = [(cmd, int(ax), int(ay), int(bx), int(by)) for cmd, ax, ay, bx, by in data]


@stopwatch
def part1():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for cmd, ax, ay, bx, by in data:
        for i in range(ax, bx + 1):
            for j in range(ay, by + 1):
                if cmd == 'turn on':
                    grid[i][j] = 1
                elif cmd == 'turn off':
                    grid[i][j] = 0
                else:
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
    return sum(sum(row) for row in grid)


@stopwatch
def part2():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for cmd, ax, ay, bx, by in data:
        for i in range(ax, bx + 1):
            for j in range(ay, by + 1):
                if cmd == 'turn on':
                    grid[i][j] += 1
                elif cmd == 'turn off':
                    grid[i][j] = max(0, grid[i][j] - 1)
                else:
                    grid[i][j] += 2
    return sum(sum(row) for row in grid)


if __name__ == '__main__':
    print(part1())  # 569999    | 1.52 seconds
    print(part2())  # 18171238  | 1.97 seconds
