from collections import Counter
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", ""), str)


@stopwatch
def part1():
    return "".join(Counter(col).most_common()[0][0] for col in zip(*data))


@stopwatch
def part2():
    return "".join(Counter(col).most_common()[-1][0] for col in zip(*data))


if __name__ == "__main__":
    print(part1())  # bjosfbce  | 0.00042 seconds
    print(part2())  # veqfxzfx  | 0.00019 seconds
