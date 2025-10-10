from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from hashlib import md5

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (), str)


@stopwatch
def part1():
    i = 0
    result = ""
    data_bytes = data.encode()

    while len(result) < 8:
        hashed = md5(data_bytes + str(i).encode()).hexdigest()
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
        hashed = md5(data_bytes + str(i).encode()).hexdigest()
        if (
            hashed[:5] == "00000"
            and hashed[5].isdigit()
            and (pos := int(hashed[5])) < 8
            and result[pos] == ""
        ):
            result[pos] = hashed[6]
            j += 1
        i += 1

    return "".join(result)


if __name__ == "__main__":
    print(part1())  # c6697b55  | 5.2764 seconds
    print(part2())  # 8c35d1ab  | 20.791 seconds
