import re

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), str)


@stopwatch
def part1():
    return sum(
        bool(
            re.search(r'(\w)\1', line)
            and len(re.findall('[aeiou]', line)) > 2
            and not re.search('ab|cd|pq|xy', line)
        ) for line in data
    )


@stopwatch
def part2():
    return sum(
        bool(
            re.search(r'(\w\w).*\1', line)
            and re.search(r'(\w).\1', line)
        ) for line in data
    )


if __name__ == '__main__':
    print(part1())  # 255   | 0.0016 seconds
    print(part2())  # 55    | 0.0020 seconds
