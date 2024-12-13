import re

from utils_anviks import parse_file_content, stopwatch
from heapq import heappush as push, heappop as pop

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n\n', '\n'), str)
data = [[tuple(map(int, re.search(r': X[+=](\d+), Y[+=](\d+)', s).groups())) for s in seq] for seq in data]


@stopwatch
def part1():
    acc = 0

    for a, b, prize in data:
        cost_loc = []
        push(cost_loc, (3, a, (1, 0)))
        push(cost_loc, (1, b, (0, 1)))
        visited = set()

        while cost_loc and (cheapest := pop(cost_loc))[1] != prize:
            cost, loc, presses = cheapest

            if (loc, presses) in visited or loc[0] > prize[0] or loc[1] > prize[1] or presses[0] > 100 or presses[1] > 100:
                continue

            visited.add((loc, presses))

            push(cost_loc, (cost + 3, (loc[0] + a[0], loc[1] + a[1]), (presses[0] + 1, presses[1])))
            push(cost_loc, (cost + 1, (loc[0] + b[0], loc[1] + b[1]), (presses[0], presses[1] + 1)))

        if cheapest and cheapest[1] == prize:
            acc += cheapest[0]

    return acc


def part2():
    pass


if __name__ == '__main__':
    print(part1())  # 26299     | 3.85 seconds
    print(part2())
