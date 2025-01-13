import re
from itertools import batched

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
with open(file) as f:
    data = list(batched(map(int, re.findall(r'\d+', f.read())), 3))


@stopwatch
def solve():
    travelled = [0] * len(data)
    points = [0] * len(data)
    for i in range(2503):
        for j, (vel, dur, rest) in enumerate(data):
            if i % (dur + rest) < dur:
                travelled[j] += vel
        lead = max(travelled)
        for j, trav in enumerate(travelled):
            if trav == lead:
                points[j] += 1
    return max(travelled), max(points)


if __name__ == '__main__':
    print(*solve())  # 2696 1084 | 0.0037 seconds
