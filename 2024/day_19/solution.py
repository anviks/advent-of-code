from functools import cache

from utils_anviks import parse_file_content, stopwatch, parse_string

file = 'data.txt'
file0 = 'example.txt'
towels, designs = parse_file_content(file, ('\n\n',), str)
towels = set(parse_string(towels, (', ',), str))
designs = parse_string(designs, ('\n',), str)


@cache
def is_possible(design: str):
    if design in towels:
        return True
    for i in range(1, len(design)):
        if design[:i] in towels and is_possible(design[i:]):
            return True
    return False


@cache
def count_possibilities(design: str):
    poss = 0
    if design in towels:
        poss += 1
    for i in range(1, len(design)):
        if design[:i] in towels and (add := count_possibilities(design[i:])):
            poss += add
    return poss


@stopwatch
def part1():
    return sum(map(is_possible, designs))


@stopwatch
def part2():
    return sum(map(count_possibilities, designs))


if __name__ == '__main__':
    print(part1())  # 313               | 0.021 seconds
    print(part2())  # 666491493769758   | 0.071 seconds
