from itertools import combinations

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), int)
data.sort(reverse=True)


@stopwatch
def part1():
    def find_combinations(idx, current_sum):
        if current_sum == 150: return 1
        if current_sum > 150 or idx == len(data): return 0

        include = find_combinations(idx + 1, current_sum + data[idx])
        exclude = find_combinations(idx + 1, current_sum)
        return include + exclude

    return find_combinations(0, 0)


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
    print(part1())  # 1638  | 0.0143 seconds
    print(part2())  # 17    | 0.00063 seconds
