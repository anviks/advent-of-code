from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


def flood_fill(cell: Cell, char: str, total_visited: set[Cell]):
    stack = [cell]
    total_visited.add(cell)
    area_cells = {cell}
    area = perimeter = 0

    while stack:
        c = stack.pop()
        area += 1

        for nb in c.neighbours('cardinal'):
            if nb not in total_visited and nb in grid and grid[nb] == char:
                total_visited.add(nb)
                area_cells.add(nb)
                stack.append(nb)
            else:
                if nb not in grid or grid[nb] != char:
                    perimeter += 1

    edges = set()

    for point in area_cells:
        for d in 1, -1, 1j, -1j:
            if point + d not in area_cells:
                edges.add((point, d))

    sides = len(edges - {(p + d * 1j, d) for p, d in edges})

    return area, perimeter, sides


@stopwatch
def part1():
    total = 0
    visited = set()
    for coord, value in grid.items():
        if coord not in visited:
            area, perimeter, sides = flood_fill(coord, value, visited)
            total += area * perimeter
    return total


@stopwatch
def part2():
    total = 0
    visited = set()
    for coord, value in grid.items():
        if coord not in visited:
            area, perimeter, sides = flood_fill(coord, value, visited)
            total += area * sides
    return total


if __name__ == '__main__':
    print(part1())  # 1434856   | 0.22 seconds
    print(part2())  # 891106
