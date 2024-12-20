from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
height, width = len(data), len(data[0])
grid = {
    complex(i, j): data[i][j]
    for i in range(len(data))
    for j in range(len(data[i]))
    if data[i][j] != '.'
}

for coord, value in grid.items():
    if value == '^':
        start = coord
        grid.pop(coord)
        break


def walk(gr: dict[complex, str]):
    loc = start
    d = -1
    visited = set()
    while (0 <= loc.imag < width and 0 <= loc.real < height) and (loc, d) not in visited:
        if loc not in gr:
            visited.add((loc, d))
            loc += d
        else:
            loc -= d
            d /= 1j
    return {p for p, _ in visited}, (loc, d) in visited


@stopwatch
def part1():
    return len(walk(grid)[0])


@stopwatch
def part2():
    return sum(walk(grid | {pos: '#'})[1] for pos in walk(grid)[0])


if __name__ == '__main__':
    print(part1())  # 5453  | 0.007 seconds
    print(part2())  # 2188  | 21.8 seconds
