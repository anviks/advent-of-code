from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = Grid(data)


def find_xmas(coord: Cell, direction: tuple[int, int]) -> bool:
    chars = iter('AMX')

    for _ in range(3):
        coord += direction
        if grid.get(coord) != next(chars):
            return False

    return True


def find_mas(coord: Cell) -> bool:
    neighbours = list(grid.neighbours(coord, 'diagonal'))
    return len(neighbours) == 4 and any(
        grid[neighbours[i - 3]] == grid[neighbours[i - 2]] == 'M' and
        grid[neighbours[i - 1]] == grid[neighbours[i]] == 'S'
        for i in range(4)
    )


@stopwatch
def part1():
    return sum(
        find_xmas(coord, dir_)
        for coord in grid.find('S')
        for dir_ in grid.neighbour_directions(coord, 'all')
    )


@stopwatch
def part2():
    return sum(find_mas(coord) for coord, value in grid.items() if value == 'A')


if __name__ == '__main__':
    print(part1())  # 2685  | 0.154 seconds
    print(part2())  # 2048  | 0.069 seconds
