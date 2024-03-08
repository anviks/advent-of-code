from collections import defaultdict

from utils_anviks import read_file, stopwatch


@read_file('data.txt', sep2='')
@stopwatch
def solution(data: list[list[str]], part: int):
    max_tiles = 0

    mapper: dict[complex, str] = {i + j * 1j: data[i][j]
                                  for i in range(len(data))
                                  for j in range(len(data[0]))}

    if part == 1:
        max_tiles = get_energized_tile_count(mapper, 1j, 0)
    else:
        for i in range(len(data)):
            max_tiles = max(max_tiles, get_energized_tile_count(mapper, 1j, i))
            max_tiles = max(max_tiles, get_energized_tile_count(mapper, -1j, i + (len(data[0]) - 1) * 1j))

        for j in range(len(data[0])):
            max_tiles = max(max_tiles, get_energized_tile_count(mapper, 1, j * 1j))
            max_tiles = max(max_tiles, get_energized_tile_count(mapper, -1, len(data) - 1 + j * 1j))

    return max_tiles


def get_energized_tile_count(tiles: dict[complex, str], direction: complex, ij: complex) -> int:
    return len(walk(tiles, direction, ij))


def walk(tile_matrix: dict[complex, str], direction: complex, ij: complex = 0, tiles: set = None) -> dict[complex, set[complex]]:
    if tiles is None:
        tiles = defaultdict(set)

    tiles[ij].add(direction)

    while True:
        match tile_matrix[ij]:
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

        if ij not in tile_matrix or direction in tiles[ij]:
            break

        tiles[ij].add(direction)

    return tiles


if __name__ == '__main__':
    print(solution(1))  # 7242  0.014s
    print(solution(2))  # 7572  3.2s
