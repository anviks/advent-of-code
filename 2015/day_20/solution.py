from numba import jit
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), int)


def find_factors(n):
    factors = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)


@jit
def factors_sum(n):
    result = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            result += 1
            if i != n // i:
                result += n // i
    return result


@stopwatch
def part1():
    i = 1
    while True:
        sum1 = factors_sum(i) * 10
        if sum1 >= data:
            return i
        i += 1


@stopwatch
def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 776160    | 2.83 seconds
    print(part2())
