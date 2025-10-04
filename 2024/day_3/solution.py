from utils_anviks import parse_file_content
import re
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (), str)


def do_multiplications(string: str):
    res = 0
    for m in re.finditer(r'mul\((\d{,3}),(\d{,3})\)', string):
        res += int(m.group(1)) * int(m.group(2))
    return res


def part1():
    return do_multiplications(data)


def part2():
    data2 = re.sub(r'don\'t\(\).*?(?:do\(\)|$)', '', data, flags=re.DOTALL)
    return do_multiplications(data2)


if __name__ == '__main__':
    print(part1())  # 175615763
    print(part2())  # 74361272
