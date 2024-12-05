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
    for i, num in enumerate(update):
        if any(fnum in update[:i] for fnum in rules_map[num]):
            return False
    return True


def find_invalid_order(update: list[int]) -> tuple[int, int] | None:
    for i, num in enumerate(update):
        for fnum in rules_map[num]:
            if fnum in update[:i]:
                return i, update[:i].index(fnum)
    return None


def part1():
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_correct_order(update)
    )


def part2():
    acc = 0

    for update in updates:
        if is_correct_order(update):
            continue

        while res := find_invalid_order(update):
            i, j = res
            update[i], update[j] = update[j], update[i]

        acc += update[len(update) // 2]

    return acc


if __name__ == '__main__':
    print(part1())
    print(part2())
