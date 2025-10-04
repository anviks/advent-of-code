from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', ' '), int)


def part1():
    safe = 0

    for report in data:
        if find_fault(report) == -1:
            safe += 1

    return safe


def part2():
    safe = 0

    for report in data:
        fault = find_fault(report)
        if fault > -1:
            for i in range(fault - 1, fault + 2):
                if find_fault(report[:i] + report[i + 1:]) == -1:
                    break
            else:
                continue

        safe += 1

    return safe


def find_fault(report: list[int]):
    direction = 0

    for i, (a, b) in enumerate(zip(report, report[1:])):
        if a == b or a > b and direction == 1 or a < b and direction == -1 or abs(a - b) > 3:
            return i
        elif a > b:
            direction = -1
        elif a < b:
            direction = 1

    return -1


if __name__ == '__main__':
    print(part1())  # 564
    print(part2())  # 604
