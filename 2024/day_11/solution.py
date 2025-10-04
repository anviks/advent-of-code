from utils_anviks import parse_file_content, stopwatch
from collections import Counter, defaultdict
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (' ',), int)


def blink(c1: Counter):
    c2 = defaultdict(int)

    for stone, count in c1.items():
        if stone == 0:
            c2[1] += c1[0]
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            s1, s2 = int(s[:len(s) // 2]), int(s[len(s) // 2:])
            c2[s1] += c1[stone]
            c2[s2] += c1[stone]
        else:
            c2[stone * 2024] += c1[stone]

    return c2


@stopwatch
def part1():
    c = Counter(data)
    for _ in range(25):
        c = blink(c)
    return sum(c.values())


@stopwatch
def part2():
    c = Counter(data)
    for _ in range(75):
        c = blink(c)
    return sum(c.values())


if __name__ == '__main__':
    print(part1())  # 187738            | 0.0025 seconds
    print(part2())  # 223767210249237   | 0.0974 seconds
