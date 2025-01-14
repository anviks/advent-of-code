import re
from itertools import batched, combinations_with_replacement

from utils_anviks import stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = list(batched(map(int, re.findall(r'-?\d+', f.read())), 5))


def share_number(total, items):
    """Generate all possible ways to share 'total' among 'items' (tuples of length 'items' and sum equal to 'total')."""
    for comb in combinations_with_replacement(range(total + 1), items - 1):
        parts = [comb[0]] + [comb[i] - comb[i - 1] for i in range(1, len(comb))] + [total - comb[-1]]
        yield tuple(parts)


@stopwatch
def solve():
    best = best_500 = 0

    for counts in share_number(100, len(data)):
        total = 1
        calories = 0

        for i in range(4):
            category = 0
            for j in range(len(data)):
                category += counts[j] * data[j][i]
            total *= max(0, category)

        for j in range(len(data)):
            calories += counts[j] * data[j][4]

        if calories == 500:
            best_500 = max(best_500, total)
        best = max(best, total)

    return best, best_500


if __name__ == '__main__':
    print(*solve())  # 13882464 11171160 | 0.49 seconds
