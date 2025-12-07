from functools import cache
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n",), str)
start = data[0].index("S")


@stopwatch
def part1():
    beam_cols = {start}
    splits = 0

    for row in range(2, len(data), 2):
        for col in beam_cols.copy():
            if data[row][col] == "^":
                beam_cols.remove(col)
                beam_cols.add(col - 1)
                beam_cols.add(col + 1)
                splits += 1

    return splits


@cache
def walk(row: int, col: int):
    paths = 0

    if row < len(data):
        if data[row][col] == "^":
            paths += walk(row + 2, col - 1)
            paths += walk(row + 2, col + 1)
        else:
            paths += walk(row + 2, col)

    return paths or 1  # Leaf nodes should return 1


@stopwatch
def part2():
    return walk(2, start)


if __name__ == "__main__":
    print(part1())  # 1622              | 0.0005 seconds
    print(part2())  # 10357305916520    | 0.0015 seconds
