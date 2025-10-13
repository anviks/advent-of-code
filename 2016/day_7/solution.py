from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch
from itertools import product, permutations
from string import ascii_lowercase

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n", re.compile(r"[\[\]]")), str)


def has_abba(s: str) -> bool:
    for i in range(len(s) - 3):
        sub = s[i : i + 4]
        if sub[0] != sub[1] and sub[:2][::-1] == sub[2:]:
            return True

    return False


@stopwatch
def part1():
    ips = 0

    for ip in data:
        for bracket in ip[1::2]:
            if has_abba(bracket):
                break
        else:
            for segment in ip[::2]:
                if has_abba(segment):
                    ips += 1
                    break

    return ips


@stopwatch
def part2():
    ips = 0

    abas = []

    for pair in permutations(ascii_lowercase, 2):
        aba = pair[0] + pair[1] + pair[0]
        abas.append(aba)

    for ip in data:
        for aba in abas:
            for segment in ip[::2]:
                if aba in segment:
                    break
            else:
                continue
            bab = aba[1] + aba[0] + aba[1]
            for bracket in ip[1::2]:
                if bab in bracket:
                    ips += 1
                    break
            else:
                continue
            break

    return ips


if __name__ == "__main__":
    print(part1())  # 118   | 0.02861 seconds
    print(part2())  # 260   | 0.22487 seconds
