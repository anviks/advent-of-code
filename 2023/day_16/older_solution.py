from collections import defaultdict

from utils_anviks.decorators import read_data, stopwatch


@read_data('data.txt', sep2='')
@stopwatch
def solution(data: list[list[str]], part: int):
    max_tiles = 0

    if part == 1:
        max_tiles = get_energized_tile_count(data, 1j, 0)
    else:
        for i in range(len(data)):
            max_tiles = max(max_tiles, get_energized_tile_count(data, 1j, i))
            max_tiles = max(max_tiles, get_energized_tile_count(data, -1j, i + (len(data[0]) - 1) * 1j))

        for j in range(len(data[0])):
            max_tiles = max(max_tiles, get_energized_tile_count(data, 1, j * 1j))
            max_tiles = max(max_tiles, get_energized_tile_count(data, -1, len(data) - 1 + j * 1j))

    return max_tiles


def get_energized_tile_count(tiles: list[list[str]], direction: complex, ij: complex) -> int:
    return len(walk(tiles, direction, ij))


def walk(tile_matrix: list[list[str]], direction: complex, ij: complex = 0, tiles: set = None) -> dict[complex, set[complex]]:
    if tiles is None:
        tiles = defaultdict(set)

    tiles[ij].add(direction)

    while True:
        match tile_matrix[round(ij.real)][round(ij.imag)]:
            case '\\':
                direction = 1j / direction
            case '/':
                direction = -1j / direction
            case '-':
                if direction in (1, -1):
                    tiles.update(walk(tile_matrix, -1j, ij, tiles))
                    direction = 1j
            case '|':
                if direction in (1j, -1j):
                    tiles.update(walk(tile_matrix, -1, ij, tiles))
                    direction = 1

        ij += direction

        if (ij.real < 0 or ij.imag < 0 or ij.real >= len(tile_matrix) or ij.imag >= len(tile_matrix[0])
                or direction in tiles[ij]):
            break

        tiles[ij].add(direction)

    return tiles


if __name__ == '__main__':
    print(solution(1))  # 7242  0.014s
    print(solution(2))  # 7572  3.75s
