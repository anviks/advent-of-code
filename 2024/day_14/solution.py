import math

from utils_anviks import parse_file_content, stopwatch, Cell

file = 'data.txt'
file0 = 'example.txt'
data = [[list(map(int, lo[2:].split(','))) for lo in loc] for loc in parse_file_content(file, ('\n', ' '), str)]
robots = [[Cell(*robot[0][::-1]), complex(*robot[1][::-1])] for robot in data]
w, h = 101, 103
cells, vectors = map(list, zip(*robots))  # type: ignore


def move(n: int = 1):
    for i in range(len(robots)):
        row, col = cells[i] + vectors[i] * n
        cells[i] = Cell(row % h, col % w)


@stopwatch
def part1():
    move(100)
    quadrants = [0] * 4

    for cell in cells:
        quadrants[0] += cell.row < h // 2 and cell.column < w // 2
        quadrants[1] += cell.row < h // 2 and cell.column > w // 2
        quadrants[2] += cell.row > h // 2 and cell.column < w // 2
        quadrants[3] += cell.row > h // 2 and cell.column > w // 2

    return math.prod(quadrants)


@stopwatch
def part2():
    for i in range(101, 10_000):
        move()
        if len(cells) == len(set(cells)):
            return i
    return None


if __name__ == '__main__':
    print(part1())  # 219512160 | 0.00051 seconds
    print(part2())  # 6398      | 1.46 seconds
