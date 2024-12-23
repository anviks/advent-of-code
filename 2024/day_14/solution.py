import math

from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell

file = 'data.txt'
file0 = 'example.txt'
data = [[list(map(int, lo[2:].split(','))) for lo in loc] for loc in parse_file_content(file, ('\n', ' '), str)]
robots = [[Cell(*robot[0][::-1]), complex(*robot[1][::-1])] for robot in data]
w, h = 101, 103


def move():
    for robot in robots:
        robot[0] += robot[1]
        robot[0].row %= h
        robot[0].column %= w

    cells = [robot[0] for robot in robots]
    quadrants = [0] * 4

    for cell in cells:
        quadrants[0] += cell.row < h // 2 and cell.column < w // 2
        quadrants[1] += cell.row < h // 2 and cell.column > w // 2
        quadrants[2] += cell.row > h // 2 and cell.column < w // 2
        quadrants[3] += cell.row > h // 2 and cell.column > w // 2

    return math.prod(quadrants)


@stopwatch
def part1():
    a = 0
    for _ in range(100):
        a = move()
    return a


@stopwatch
def part2():
    for i in range(100, 10_000):
        cells = [robot[0] for robot in robots]
        move()
        if len(cells) == len(set(cells)):
            return i
    return None


if __name__ == '__main__':
    print(part1())  # 219512160 | 0.07 seconds
    print(part2())  # 6398      | 5.05 seconds
