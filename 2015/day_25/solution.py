from utils_anviks import stopwatch

row, column = 2978, 3083


def next_code(code: int):
    return code * 252533 % 33554393


@stopwatch
def part1():
    n = sum(range(column + 1))
    for i in range(row - 1):
        n += column + i
    code = 20151125
    for _ in range(n - 1):
        code = next_code(code)
    return code


if __name__ == '__main__':
    print(part1())  # 2650453   | 2.41 seconds
