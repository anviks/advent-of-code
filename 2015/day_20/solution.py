import numpy as np
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), int)


@stopwatch
def part1():
    presents = np.zeros(data // 10, dtype=int)
    for i in range(1, data // 10):
        presents[i::i] += i * 10
        if presents[i] >= data:
            return i


@stopwatch
def part2():
    presents = np.zeros(data // 10, dtype=int)
    for i in range(1, data // 10):
        presents[i:i*50:i] += i * 11
        if presents[i] >= data:
            return i


if __name__ == '__main__':
    print(part1())  # 776160    | 1.76 seconds
    print(part2())  # 786240    | 1.59 seconds
