import math

from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', 'x'), int)


@stopwatch
def part1():
    acc = 0
    for l, w, h in data:
        acc += 2 * l * w + 2 * w * h + 2 * h * l
        acc += min(l * w, w * h, h * l)
    return acc


@stopwatch
def part2():
    acc = 0
    for l, w, h in data:
        acc += 2 * l + 2 * w + 2 * h - max(2 * l, 2 * w, 2 * h)
        acc += l * w * h
    return acc


if __name__ == '__main__':
    print(part1())  # 1586300   | 0.00025 seconds
    print(part2())  # 3737498   | 0.00019 seconds
