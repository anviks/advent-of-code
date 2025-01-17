from itertools import combinations

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), int)


@stopwatch
def part1():
    result = 0
    for r in range(1, len(data) + 1):
        result += sum(1 for combo in combinations(data, r) if sum(combo) == 150)
    return result


@stopwatch
def part2():
    containers = float('inf')
    ways_to_fill = 0

    for r in range(1, len(data) + 1):
        if r > containers:
            break
        for combo in combinations(data, r):
            if sum(combo) == 150:
                containers = r
                ways_to_fill += 1

    return ways_to_fill


if __name__ == '__main__':
    print(part1())  # 1638  | 0.165 seconds
    print(part2())  # 17    | 0.00063 seconds
