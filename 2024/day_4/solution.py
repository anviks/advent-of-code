from utils_anviks import parse_file_content

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)
grid = {
    complex(i, j): data[i][j]
    for i in range(len(data))
    for j in range(len(data[i]))
}


def find_xmas(coord: complex, direction: complex) -> bool:
    chars = ['X', 'M', 'A']

    for _ in range(3):
        coord += direction
        value = grid.get(coord)
        if value is None or value != chars.pop():
            return False

    return True


def find_mas(coord: complex) -> bool:
    diagonals = [-1 - 1j, -1 + 1j, 1 + 1j, 1 - 1j, -1 - 1j]

    for a, b in zip(diagonals, diagonals[1:]):
        if grid.get(coord + a) == grid.get(coord + b) == 'M' and grid.get(coord - a) == grid.get(coord - b) == 'S':
            return True

    return False


def part1():
    xmas_count = 0

    for coord, value in grid.items():
        if value == 'S':
            for dir_x in range(-1, 2):
                for dir_y in range(-1, 2):
                    if dir_x == dir_y == 0:
                        continue
                    xmas_count += find_xmas(coord, complex(dir_x, dir_y))

    return xmas_count


def part2():
    mas_count = 0

    for coord, value in grid.items():
        if value == 'A':
            mas_count += find_mas(coord)

    return mas_count


if __name__ == '__main__':
    print(part1())  # 2685
    print(part2())  # 2048
