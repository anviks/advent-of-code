from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, (',', '-'), int)


@stopwatch
def part1():
    x = 0
    for start, end in data:
        for i in range(start, end + 1):
            str_i = str(i)
            len_i = len(str_i)
            if len_i % 2 == 0 and str_i[:len_i//2] == str_i[len_i//2:]:
                x += i

    return x


def is_invalid(s: str):
    len_s = len(s)
    
    for i in range(1, len_s // 2 + 1):
        if len_s % i != 0:
            continue

        for j in range(len_s // i - 1):
            if s[j*i:j*i+i] != s[j*i+i:j*i+i+i]:
                break
        else:
            return True
    
    return False

@stopwatch
def part2():
    x = 0
    for start, end in data:
        for i in range(start, end + 1):
            if is_invalid(str(i)):
                x += i

    return x


if __name__ == '__main__':
    print(part1()) # 18893502033    | 0.527 seconds
    print(part2()) # 26202168557    | 2.792 seconds
