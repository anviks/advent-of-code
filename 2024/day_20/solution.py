from heapq import heappop, heappush
from itertools import combinations, count

from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)

start, end, direction = grid.find_first('S'), grid.find_first('E'), 1j
uid = count()
todo = []
costs: dict[Cell, int] = {}
heappush(todo, (0, next(uid), start, direction))
while todo:
    cost, _, loc, d = heappop(todo)  # type: int, int, Cell, complex
    costs[loc] = cost
    if loc == end:
        break
    for dir_ in (d, d * 1j, d * -1j):
        new_loc = loc + dir_
        if grid[new_loc] != '#':
            heappush(todo, (cost + 1, next(uid), new_loc, dir_))


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
    print(part1())  # 1387      | 7.99 seconds
    print(part2())  # 1015092   | 8.10 seconds
