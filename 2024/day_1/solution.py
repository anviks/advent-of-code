from collections import Counter

from utils_anviks import parse_file_content

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', '   '), int)
data = list(zip(*data))


def part1():
    data1 = [sorted(a) for a in data]
    data1 = list(zip(*data1))
    result = sum(abs(a - b) for a, b in data1)

    return result


def part2():
    c = Counter(data[1])
    acc = 0

    for n in data[0]:
        acc += c[n] * n

    return acc


if __name__ == '__main__':
    print(part1())  # 1506483
    print(part2())  # 23126924
