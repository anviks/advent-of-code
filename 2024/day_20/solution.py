from itertools import combinations

from utils_anviks import parse_file_content, stopwatch, Grid, Cell
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', ''), str)
grid = Grid(data)

start, end, direction = grid.find_first('S'), grid.find_first('E'), 1j
loc, d = start, direction
costs: dict[Cell, int] = {loc: 0}
while loc != end:
    for dir_ in (d, d * 1j, d * -1j):
        if grid[loc + dir_] != '#':
            costs[loc + dir_], loc, d = costs[loc] + 1, loc + dir_, dir_
            break


def solve(max_cheat: int):
    possibilities = 0

    for (cell_a, cost_a), (cell_b, cost_b) in combinations(costs.items(), 2):
        distance = cell_a.manhattan_distance(cell_b)
        if distance <= max_cheat and abs(cost_a - cost_b) - distance >= 100:
            possibilities += 1

    return possibilities


@stopwatch
def part1():
    return solve(2)


@stopwatch
def part2():
    return solve(20)


if __name__ == '__main__':
    print(part1())  # 1387      | 3.71 seconds
    print(part2())  # 1015092   | 3.81 seconds
