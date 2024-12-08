from collections import defaultdict
from itertools import permutations

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), str)
grid = {
    complex(i, j): data[i][j]
    for i in range(len(data))
    for j in range(len(data[i]))
}

antennas = defaultdict(list)
for k, v in grid.items():
    if v != '.':
        antennas[v].append(k)


def part1():
    antinodes = set()

    for ant, loc in antennas.items():
        for a, b in permutations(loc, 2):
            antinode = a + (a - b)
            if antinode in grid:
                antinodes.add(antinode)

    return len(antinodes)



def part2():
    antinodes = set()

    for ant, loc in antennas.items():
        for a, b in permutations(loc, 2):
            antinodes.add(a)
            antinodes.add(b)
            diff = a - b
            antinode = a + diff
            while antinode in grid:
                antinodes.add(antinode)
                antinode += diff

    return len(antinodes)


if __name__ == '__main__':
    print(part1())
    print(part2())
