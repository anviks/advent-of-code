from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
import numpy as np

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ('\n', ''), str)

def surrounding_rolls(row: int, col: int) -> int:
    rolls = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            r, c = row + i, col + j
            if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == '@':
                rolls += 1
    return rolls

@stopwatch
def part1():
    accessible = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            accessible += data[i][j] == '@' and surrounding_rolls(i, j) < 4
    
    return accessible


@stopwatch
def part2():
    accessible = 0
    # temp_accessible = -1

    # while temp_accessible != 0:
    #     temp_accessible = 0

    #     for i in range(len(data)):
    #         for j in range(len(data[i])):
    #             temp_accessible += data[i][j] == '@' and surrounding_rolls(i, j) < 4

    #     accessible += temp_accessible

    return accessible


if __name__ == "__main__":
    print(part1())  # 1491
    print(part2())
