from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('',), str)
directions = {
    '^': -1,
    'v': 1,
    '<': -1j,
    '>': 1j,
}


@stopwatch
def part1():
    current = 0
    i = 0
    seen = set()
    while i < len(data):
        seen.add(current)
        current += directions[data[i]]
        i += 1
    return len(seen)


@stopwatch
def part2():
    santa = robot = 0
    i = 1
    seen = set()
    while i < len(data):
        seen.add(santa)
        seen.add(robot)
        santa += directions[data[i - 1]]
        robot += directions[data[i]]
        i += 2
    return len(seen)


if __name__ == '__main__':
    print(part1())  # 2592  | 0.0023 seconds
    print(part2())  # 2360  | 0.0021 seconds
