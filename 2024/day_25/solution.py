from utils_anviks import parse_file_content, stopwatch
from itertools import product

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n\n', '\n', ''), str)


def compress(schematic: list[list[str]]):
    return [col.count('#') - 1 for col in zip(*schematic)]


locks = [compress(schem) for schem in data if schem[0] == ['#'] * 5]
keys = [compress(schem) for schem in data if schem[6] == ['#'] * 5]


@stopwatch
def part1():
    return sum(
        all(lock[i] + key[i] <= 5 for i in range(5))
        for lock, key in product(locks, keys)
    )


if __name__ == '__main__':
    print(part1())  # 3495  | 0.030 seconds
