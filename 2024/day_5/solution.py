from collections import defaultdict

from utils_anviks import parse_file_content, parse_string, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n\n',), str)
rules, updates = data
rules = parse_string(rules, ('\n', '|'), int)
updates = parse_string(updates, ('\n', ','), int)

rules_map = defaultdict(list)
for rule in rules:
    rules_map[rule[0]].append(rule[1])


def is_correct_order(update: list[int]):
    for i, n in enumerate(update):
        following_nums = rules_map[n]
        for fnum in following_nums:
            if fnum in update[:i]:
                return False

    return True


def part1():
    acc = 0

    for update in updates:
        if is_correct_order(update):
            acc += update[len(update) // 2]

    return acc


def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
