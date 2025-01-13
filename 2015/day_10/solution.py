from functools import cache

from utils_anviks import stopwatch


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
def part1(digits: str):
    for _ in range(40):
        digits = look_and_say(digits)
    return len(digits)


@stopwatch
def part2(digits: str):
    for _ in range(50):
        digits = look_and_say(digits)
    return len(digits)


if __name__ == '__main__':
    input_ = '1321131112'
    print(part1(input_))  # 492982    | 0.32 seconds
    print(part2(input_))  # 6989950   | 4.35 seconds
