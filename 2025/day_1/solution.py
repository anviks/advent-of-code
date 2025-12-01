from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ('\n',), str)


@stopwatch
def part1():
    current = 50
    password = 0

    for rotation in data:
        direction, clicks = rotation[0], int(rotation[1:])
        if direction == 'L':
            clicks = -clicks

        current = (current + clicks + 100) % 100

        if current == 0:
            password += 1

    return password


@stopwatch
def part2():
    current = 50
    password = 0

    for rotation in data:
        direction, clicks = rotation[0], int(rotation[1:])
        if direction == 'L':
            clicks = -clicks

        for _ in range(clicks):
            current += 1
            if current % 100 == 0:
                password += 1

        for _ in range(0, clicks, -1):
            current -= 1
            if current % 100 == 0:
                password += 1

    return password


if __name__ == '__main__':
    print(part1())  # 984   | 0.0009 seconds
    print(part2())  # 5657  | 0.035 seconds
