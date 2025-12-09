from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from itertools import combinations

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ('\n', ','), int)


@stopwatch
def part1():
    largest = 0
    for tile1, tile2 in combinations(data, 2):
        area = (abs(tile2[0] - tile1[0]) + 1) * (abs(tile2[1] - tile1[1]) + 1)
        largest = max(largest, area)
    return largest


@stopwatch
def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
