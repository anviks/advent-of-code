from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
_data = parse_file_content(file_path, ("\n",), str)
data = []

for triangle in _data:
    split_triangle = re.split(r" +", triangle)
    if split_triangle[0] == "":
        split_triangle = split_triangle[1:]
    sides = [int(side) for side in split_triangle]
    data.append(sides)


@stopwatch
def part1():
    possible = 0

    for sides in data:
        sides = sorted(sides)
        possible += sum(sides[:2]) > sides[2]

    return possible


@stopwatch
def part2():
    possible = 0

    for j in range(3):
        for i in range(len(data) // 3):
            sides = []
            for k in range(3):
                sides.append(data[i * 3 + k][j])
            sides.sort()
            possible += sum(sides[:2]) > sides[2]

    return possible


if __name__ == "__main__":
    print(part1())  # 983
    print(part2())  # 1836
