from functools import cache

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), str)


def get_chunks(digits: str):
    chunks = []
    l = 0
    for r in range(1, len(digits)):
        if digits[r] != digits[l]:
            chunks.append((r - l, digits[l]))
            l = r
    chunks.append((len(digits) - l, digits[l]))
    return chunks


@cache
def look_and_say(digits: str):
    chunks = get_chunks(digits)
    digz = []
    for count, digit in chunks:
        digz.append(str(count))
        digz.append(digit)
    return ''.join(digz)


@stopwatch
def part1():
    result = data
    for _ in range(40):
        result = look_and_say(result)
    return len(result)


@stopwatch
def part2():
    result = data
    for _ in range(50):
        result = look_and_say(result)
    return len(result)


if __name__ == '__main__':
    print(part1())  # 492982    | 0.32 seconds
    print(part2())  # 6989950   | 4.35 seconds
