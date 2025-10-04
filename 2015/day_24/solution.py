import math
from itertools import combinations

from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n',), int)


@stopwatch
def solve(part: int):
    group_weight = sum(data) // (2 + part)
    for i in range(2, len(data)):
        prods = []
        for combo in (c for c in combinations(data, i) if sum(c) == group_weight):
            prods.append(math.prod(combo))
        if prods:
            return min(prods)


if __name__ == '__main__':
    print(solve(1))  # 11846773891  | 0.079 seconds
    print(solve(2))  # 80393059     | 0.003 seconds
