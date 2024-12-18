from collections import deque

from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ','), int)
grid = Grid.from_function(71, 71, lambda i, j: '#' if [j, i] in data[:1024] else '.')
# At first, I solved part 2 by just changing how many bytes I include in the grid, essentially doing a manual binary search
# to find the first byte that causes the path to be blocked (part1 would return None).
# That was by far the quickest way to find out the answer.


def part1():
    start = Cell(0, 0)
    target = Cell(70, 70)
    queue = deque([(0, start)])
    visited = {start}

    while queue:
        length, pos = queue.popleft()

        if pos == target:
            return length

        for nb in grid.neighbours(pos, 'cardinal'):
            if grid[nb] != '#' and nb not in visited:
                visited.add(nb)
                queue.append((length + 1, nb))


@stopwatch
def part2():
    global grid
    grid2 = grid.copy()
    low = 1024
    high = len(data)
    while low < high:
        mid = (low + high) // 2
        grid = grid2.copy()
        for i, j in data[1024:mid]:
            grid[j, i] = '#'
        if part1():
            low = mid + 1
        else:
            high = mid
    i, j = data[low - 1]
    return f'{i},{j}'


if __name__ == '__main__':
    print(part1())  # 272       | 0.024 seconds
    print(part2())  # 16,44     | 0.040 seconds
