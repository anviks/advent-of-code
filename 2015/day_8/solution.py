import json

from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n',), str)


@stopwatch
def part1():
    return sum(len(s) - len(eval(s)) for s in data)


@stopwatch
def part2():
    return sum(len(json.dumps(s)) - len(s) for s in data)


if __name__ == '__main__':
    print(part1())  # 1333  | 0.0018 seconds
    print(part2())  # 2046  | 0.00015 seconds
