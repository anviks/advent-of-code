import numpy as np
from scipy.signal import convolve2d
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)


@stopwatch
def solution(part: int):
    grid = np.array([[cell == '#' for cell in row] for row in data])
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    for _ in range(100):
        neighbor_counts = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
        grid = (grid & ((neighbor_counts == 2) | (neighbor_counts == 3))) | (~grid & (neighbor_counts == 3))
        if part == 2:
            grid[::99, ::99] = 1

    return np.sum(grid)


if __name__ == '__main__':
    print(solution(1))  # 768   | 0.31 seconds
    print(solution(2))  # 781   | 0.31 seconds
