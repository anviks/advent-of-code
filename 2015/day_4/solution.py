import hashlib

from utils_anviks import stopwatch

key = 'yzbqklnj'


@stopwatch
def part1():
    i = 1
    while hashlib.md5((key + str(i)).encode()).hexdigest()[:5] != '00000':
        i += 1
    return i


@stopwatch
def part2():
    i = 1
    while hashlib.md5((key + str(i)).encode()).hexdigest()[:6] != '000000':
        i += 1
    return i


if __name__ == '__main__':
    print(part1())  # 282749    | 0.35 seconds
    print(part2())  # 9962624   | 12.4 seconds
