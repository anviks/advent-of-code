from pathlib import Path
from utils_anviks import parse_file_content, stopwatch, parse_string

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n\n",), str)
ranges = parse_string(data[0], ("\n", "-"), int)
available = parse_string(data[1], ("\n",), int)


@stopwatch
def part1():
    fresh = 0

    for ingredient in available:
        for start, stop in ranges:
            if start <= ingredient <= stop:
                fresh += 1
                break

    return fresh


@stopwatch
def part2():
    sorted_ranges = sorted(ranges)
    i = 0

    while i < len(sorted_ranges) - 1:
        # Connect overlapping pairs and pairs like [11, 20] and [21, 30]
        if sorted_ranges[i][1] + 1 >= sorted_ranges[i + 1][0]:
            sorted_ranges[i] = [
                sorted_ranges[i][0],
                max(sorted_ranges[i][1], sorted_ranges[i + 1][1]),
            ]
            sorted_ranges.pop(i + 1)
        else:
            i += 1

    return sum(stop - start + 1 for start, stop in sorted_ranges)


if __name__ == "__main__":
    print(part1())  # 707               | 0.0038 seconds
    print(part2())  # 361615643045059   | 0.00009 seconds
