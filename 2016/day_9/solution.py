from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, (), str)


def solve(s: str, *, recurse: bool = False):
    total = 0
    pointer = 0

    def consume_number():
        nonlocal pointer
        num = ""
        while pointer < len(s) and s[pointer].isdigit():
            num += s[pointer]
            pointer += 1
        return int(num)

    while pointer < len(s):
        char = s[pointer]

        if char == "(":
            pointer += 1  # (
            sub_len = consume_number()
            pointer += 1  # x
            times = consume_number()
            pointer += 1  # )

            if recurse:
                total += solve(s[pointer : pointer + sub_len], recurse=True) * times
            else:
                total += sub_len * times

            pointer += sub_len
        else:
            total += 1
            pointer += 1

    return total


@stopwatch
def part1():
    return solve(data, recurse=False)


@stopwatch
def part2():
    return solve(data, recurse=True)


if __name__ == "__main__":
    print(part1())  # 123908        | 0.00005 seconds
    print(part2())  # 10755693147   | 0.0017 seconds
