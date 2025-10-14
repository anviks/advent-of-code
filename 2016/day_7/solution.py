from pathlib import Path
import re
from more_itertools import sliding_window
from utils_anviks import parse_file_content, stopwatch
from itertools import permutations
from string import ascii_lowercase

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", re.compile(r"[\[\]]")), str)


def has_abba(s: str) -> bool:
    for sub in sliding_window(s, 4):
        a, b, _, _ = sub
        if a != b and (a, b, b, a) == sub:
            return True

    return False


@stopwatch
def part1():
    return sum(
        has_abba(";".join(ip[::2])) and not has_abba(";".join(ip[1::2])) for ip in data
    )


@stopwatch
def part2():
    ips = 0
    abas = [a + b + a for a, b in permutations(ascii_lowercase, 2)]

    for ip in data:
        for aba in abas:
            if aba not in ";".join(ip[::2]):
                continue

            bab = aba[1] + aba[0] + aba[1]
            if bab in ";".join(ip[1::2]):
                ips += 1
                break

    return ips


if __name__ == "__main__":
    print(part1())  # 118   | 0.013 seconds
    print(part2())  # 260   | 0.22 seconds
