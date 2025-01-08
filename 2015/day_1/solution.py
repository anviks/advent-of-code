from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), str)


@stopwatch
def part1():
    return data.count('(') - data.count(')')


@stopwatch
def part2():
    floor = 0
    for i, char in enumerate(data, 1):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i


if __name__ == '__main__':
    print(part1())  # 0.000046 seconds
    print(part2())  # 0.00015 seconds
