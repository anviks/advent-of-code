import re
from itertools import batched

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = re.findall(r'(\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', f.read())
print(data)

message = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


@stopwatch
def part1():
    for i, known_info in enumerate(data, 1):
        can_be = True

        for item, count in batched(known_info, 2):
            can_be = can_be and message.get(item) == int(count)

        if can_be:
            return i


@stopwatch
def part2():
    for i, known_info in enumerate(data, 1):
        can_be = True

        for item, count in batched(known_info, 2):
            can_be = can_be and (
                    item in ('cats', 'trees') and message.get(item, 0) < int(count) or
                    item in ('pomeranians', 'goldfish') and message.get(item, float('inf')) > int(count) or
                    item not in ('pomeranians', 'goldfish', 'cats', 'trees') and message.get(item) == int(count)
            )

        if can_be:
            return i


if __name__ == '__main__':
    print(part1())
    print(part2())
