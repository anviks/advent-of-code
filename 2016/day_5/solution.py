from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from hashlib import md5
import random

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (), str)


class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_hash_hex(base_bytes: bytes, num: int):
    return md5(base_bytes + str(num).encode()).hexdigest()


@stopwatch
def part1():
    i = 0
    result = ""
    data_bytes = data.encode()

    while len(result) < 8:
        hashed = get_hash_hex(data_bytes, i)
        if hashed[:5] == "00000":
            result += hashed[5]
        i += 1

    return result


@stopwatch
def part2():
    i = j = 0
    result = [""] * 8
    data_bytes = data.encode()

    while j < 8:
        hashed = get_hash_hex(data_bytes, i)
        if (
            hashed[:5] == "00000"
            and hashed[5].isdigit()
            and (pos := int(hashed[5])) < 8
            and result[pos] == ""
        ):
            result[pos] = hashed[6]
            j += 1
        i += 1

        if i % 30000 == 0:
            for char in result:
                if char == "":
                    print(
                        f"{Color.WARNING}{random.randint(0, 15):x}{Color.ENDC}", end=""
                    )
                else:
                    print(Color.OKGREEN + char + Color.ENDC, end="")

            print("\r", end="")

    return "".join(result)


if __name__ == "__main__":
    print(part1())  # c6697b55  | 5.2764 seconds
    print(part2())  # 8c35d1ab  | 20.791 seconds
