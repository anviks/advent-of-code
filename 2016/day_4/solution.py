from collections import Counter
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from string import ascii_lowercase

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n",), str)


def compute_checksum(name: str):
    counter = Counter(name.replace("-", ""))
    letters = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5]
    return "".join(l[0] for l in letters)


def rotate(n: int, s: str) -> str:
    n %= 26
    lookup = str.maketrans(ascii_lowercase, ascii_lowercase[n:] + ascii_lowercase[:n])
    return s.translate(lookup)


@stopwatch
def part1():
    id_sum = 0

    for room in data:
        room, checksum = room[:-1].split("[")
        name, _id = room.rsplit("-", 1)

        if checksum == compute_checksum(name):
            id_sum += int(_id)

    return id_sum


@stopwatch
def part2():
    for room in data:
        name, _id = room[:-1].split("[")[0].rsplit("-", 1)
        decrypted_name = rotate(int(_id), name)

        if "north" in decrypted_name:
            return _id


if __name__ == "__main__":
    print(part1())  # 137896
    print(part2())  # 501
