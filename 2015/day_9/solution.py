from itertools import permutations

from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', ' = '), str)
distances = {}
cities = set()

for cit, dist in data:
    a, b = cit.split(' to ')
    distances[a, b] = distances[b, a] = int(dist)
    cities.add(a)
    cities.add(b)


@stopwatch
def part1():
    best = float('inf')
    for perm in permutations(cities):
        dis = 0
        for pair in zip(perm, perm[1:]):
            dis += distances[pair]
        best = min(best, dis)
    return best


@stopwatch
def part2():
    best = float('-inf')
    for perm in permutations(cities):
        dis = 0
        for pair in zip(perm, perm[1:]):
            dis += distances[pair]
        best = max(best, dis)
    return best


if __name__ == '__main__':
    print(part1())  # 117   | 0.043 seconds
    print(part2())  # 909   | 0.043 seconds
