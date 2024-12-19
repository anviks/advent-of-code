from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


def flood_fill(cell: Cell, char: str, visited: set[Cell]):
    stack = [cell]
    visited.add(cell)
    area = perimeter = 0

    while stack:
        c = stack.pop()
        area += 1

        for nb in c.neighbours('cardinal'):
            if nb not in visited and nb in grid and grid[nb] == char:
                visited.add(nb)
                stack.append(nb)
            else:
                if nb not in grid or grid[nb] != char:
                    perimeter += 1

    return area, perimeter


@stopwatch
def part1():
    total = 0
    visited = set()
    for coord, value in grid.items():
        if coord not in visited:
            area, perimeter = flood_fill(coord, value, visited)
            total += area * perimeter
    return total


def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 1434856   | 0.22 seconds
    print(part2())
