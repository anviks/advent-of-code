import re
from itertools import permutations

from utils_anviks import stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = re.findall(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.', f.read())


def get_useful_data():
    people = {data[i][0] for i in range(len(data))}
    happiness_map = {}
    for a, sign, n, b in data:
        num = int(n)
        if sign == 'lose':
            num = -num
        happiness_map[a, b] = num
    return people, happiness_map


def get_optimal_happiness(people: set[str], happiness_map: dict[tuple[str, str], int]):
    best = 0

    for perm in permutations(people):
        happiness = 0
        for pair in zip(perm, perm[1:]):
            happiness += happiness_map[pair]
            happiness += happiness_map[pair[::-1]]
        happiness += happiness_map[perm[-1], perm[0]]
        happiness += happiness_map[perm[0], perm[-1]]
        best = max(best, happiness)

    return best


@stopwatch
def part1():
    return get_optimal_happiness(*get_useful_data())


@stopwatch
def part2():
    people, happiness_map = get_useful_data()
    for p in people:
        happiness_map[p, 'me'] = 0
        happiness_map['me', p] = 0
    people.add('me')
    return get_optimal_happiness(people, happiness_map)


if __name__ == '__main__':
    print(part1())  # 709   | 0.095 seconds
    print(part2())  # 668   | 0.92 seconds
