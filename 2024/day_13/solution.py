import re

import numpy as np
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n\n', '\n'), str)
data = [[tuple(map(int, re.search(r': X[+=](\d+), Y[+=](\d+)', s).groups())) for s in seq] for seq in data]


@stopwatch
def solve(part: int):
    tokens = 0
    for a, b, prize in data:
        matrix = np.array([*zip(a, b)])
        prize_vector = np.array(prize) + (part == 2) * 10000000000000
        result = np.round(np.linalg.solve(matrix, prize_vector))
        if (result @ matrix.transpose() == prize_vector).all():
            tokens += int(result @ (3, 1))
    return tokens


if __name__ == '__main__':
    print(solve(1))  # 26299               | 0.007 seconds
    print(solve(2))  # 107824497933339     | 0.007 seconds
