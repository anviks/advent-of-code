from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from itertools import combinations, pairwise

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", ","), int)
green = [sorted(pair) for pair in pairwise(data + [data[0]])]


@stopwatch
def part1():
    largest = 0
    for (col1, row1), (col2, row2) in combinations(data, 2):
        area = (abs(col2 - col1) + 1) * (abs(row2 - row1) + 1)
        largest = max(largest, area)
    return largest


@stopwatch
def part2():
    largest = 0
    for (col1, row1), (col2, row2) in combinations(data, 2):
        if col1 > col2:
            col1, col2 = col2, col1
        if row1 > row2:
            row1, row2 = row2, row1

        area = (col2 - col1 + 1) * (row2 - row1 + 1)

        if area > largest:
            for (g_col1, g_row1), (g_col2, g_row2) in green:
                # If green line intersects the red area, then the area isn't valid
                if g_col1 < col2 and g_col2 > col1 and g_row1 < row2 and g_row2 > row1:
                    break
            else:
                largest = area

    return largest


if __name__ == "__main__":
    print(part1())  # 4782896435    | 0.04 seconds
    print(part2())  # 1540060480    | 0.77 seconds
