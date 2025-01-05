from collections import defaultdict
from heapq import heappop, heappush
from itertools import count

from utils_anviks import parse_file_content, stopwatch, Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


@stopwatch
def part1():
    start, end, direction = grid.find_first('S'), grid.find_first('E'), 1j
    uid = count()
    paths = []
    visited = set()
    heappush(paths, (0, next(uid), start, direction))
    while paths:
        cost, _, loc, d = heappop(paths)
        if loc == end:
            return cost
        if loc in visited:
            continue
        visited.add(loc)
        for dir_ in (d, d * 1j, d * -1j):
            if grid[loc + dir_] != '#':
                new_cost = cost + 1 + 1000 * (dir_ != d)
                heappush(paths, (new_cost, next(uid), loc + dir_, dir_))


@stopwatch
def part2():
    start, end, direction = grid.find_first('S'), grid.find_first('E'), 1j
    uid = count()
    todo = []
    best_visited = set()
    best = float('inf')
    costs = defaultdict(lambda: float('inf'))
    heappush(todo, (0, next(uid), start, direction, [start]))
    while todo:
        cost, _, loc, d, path = heappop(todo)
        if cost > costs[loc, d]:
            continue
        costs[loc, d] = cost
        if loc == end:
            if cost <= best:
                best_visited.update(path)
                best = cost
            continue
        for dir_ in (d, d * 1j, d * -1j):
            new_loc = loc + dir_
            if grid[new_loc] != '#':
                new_cost = cost + 1 + 1000 * (dir_ != d)
                heappush(todo, (new_cost, next(uid), new_loc, dir_, path + [new_loc]))
    return len(best_visited)


if __name__ == '__main__':
    print(part1())  # 95444 | 0.03 seconds
    print(part2())  # 513   | 2.91 seconds
