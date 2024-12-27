from heapq import heappop, heappush

from utils_anviks import parse_file_content, stopwatch

from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


@stopwatch
def part1():
    start, end, direction = grid.find_first('S'), grid.find_first('E'), 1j
    uid = 1
    paths = []
    visited = set()
    heappush(paths, (0, 0, start, direction))
    while paths:
        cost, _, loc, d = heappop(paths)
        if loc == end:
            return cost
        if loc in visited:
            continue
        visited.add(loc)
        for dir_ in (d, d * 1j, d * -1j):
            if grid[loc + dir_] != '#':
                uid += 1
                heappush(paths, (cost + 1 + 1000 * (dir_ != d), uid, loc + dir_, dir_))


def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 95444 | 0.060 seconds
    print(part2())
