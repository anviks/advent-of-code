from collections import defaultdict
from random import shuffle

from utils_anviks import parse_file_content, parse_string, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n\n',), str)
replacements = parse_string(data[0], ('\n', ' => '), str)
replacement_dict = defaultdict(list)

for k, v in replacements:
    replacement_dict[k].append(v)


@stopwatch
def part1():
    l, r = 0, 1
    molecule = data[1]
    possibilities = set()

    while r < len(molecule):
        if molecule[r].islower():
            r += 1

        for repl in replacement_dict[molecule[l:r]]:
            possibilities.add(molecule[:l] + repl + molecule[r:])

        l = r
        r += 1

    return len(possibilities)


@stopwatch
def part2():
    molecule = data[1]
    current = molecule
    steps = 0

    while current != 'e':
        start = current
        for src, target in replacements:
            if target not in current:
                continue

            current = current.replace(target, src, 1)
            steps += 1

        if start == current:
            # No replacements were possible, reset and shuffle
            current = molecule
            steps = 0
            shuffle(replacements)

    return steps


if __name__ == '__main__':
    print(part1())
    print(part2())
