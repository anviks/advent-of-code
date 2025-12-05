from pathlib import Path
from utils_anviks import parse_file_content, stopwatch, parse_string

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n\n",), str)
ranges = [
    range(start, end + 1) for start, end in parse_string(data[0], ("\n", "-"), int)
]
available = parse_string(data[1], ("\n",), int)


@stopwatch
def part1():
    fresh = 0

    for ingredient in available:
        for rang in ranges:
            if ingredient in rang:
                fresh += 1
                break

    return fresh


@stopwatch
def part2():
    sorted_ranges = sorted(ranges, key=lambda x: (x.start, x.stop))

    i = 0

    while i < len(sorted_ranges) - 1:
        if sorted_ranges[i].stop >= sorted_ranges[i + 1].start:
            sorted_ranges[i] = range(
                sorted_ranges[i].start,
                max(sorted_ranges[i].stop, sorted_ranges[i + 1].stop),
            )
            sorted_ranges.pop(i + 1)
        else:
            i += 1

    fresh = 0

    for rang in sorted_ranges:
        fresh += rang.stop - rang.start

    return fresh


if __name__ == "__main__":
    print(part1())  # 707               | 0.0045 seconds
    print(part2())  # 361615643045059   | 0.0001 seconds
