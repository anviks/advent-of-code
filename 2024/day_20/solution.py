from heapq import heappop, heappush
from itertools import combinations, count

from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


@stopwatch
def part1():
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

    acc = 0

    for (cell_a, cost_a), (cell_b, cost_b) in combinations(costs.items(), 2):
        if cell_a.euclidean_distance(cell_b) == 2 and abs(cost_a - cost_b) - 2 >= 100:
            acc += 1

    return acc


def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 1387  | 17.4 seconds
    print(part2())
