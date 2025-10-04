import json
import re

from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (), str)


@stopwatch
def part1():
    return sum(map(int, re.findall(r'-?\d+', data)))


def get_sum(obj: list | dict):
    result = 0

    def process_value(value):
        nonlocal result
        if isinstance(value, list | dict):
            result += get_sum(value)
        elif isinstance(value, int):
            result += value

    if isinstance(obj, list):
        for val in obj:
            process_value(val)
        return result
    elif isinstance(obj, dict):
        for val in obj.values():
            if val == 'red':
                return 0
            process_value(val)
        return result


@stopwatch
def part2():
    obj = json.loads(data)
    return get_sum(obj)


if __name__ == '__main__':
    print(part1())  # 111754    | 0.0011 seconds
    print(part2())  # 65402     | 0.0012 seconds
