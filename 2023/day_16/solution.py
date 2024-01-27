from __future__ import annotations

from collections import defaultdict
from enum import Enum

from utils_anviks.decorators import read_data, stopwatch


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    def apply(self, i: int, j: int) -> tuple[int, int]:
        di, dj = self.value
        return i + di, j + dj

    def apply_backslash(self) -> Direction:
        return {
            self.RIGHT: self.DOWN,
            self.DOWN: self.RIGHT,
            self.LEFT: self.UP,
            self.UP: self.LEFT,
        }[self]

    def apply_slash(self) -> Direction:
        return {
            self.RIGHT: self.UP,
            self.UP: self.RIGHT,
            self.LEFT: self.DOWN,
            self.DOWN: self.LEFT,
        }[self]


def get_energized_tile_count(tiles: list[list[str]], direction: Direction, i: int, j: int) -> int:
    return len(walk(tiles, direction, i, j))


@read_data('data.txt', sep2='')
@stopwatch
def solution(data: list[list[str]], part: int):
    max_tiles = 0

    if part == 1:
        max_tiles = get_energized_tile_count(data, Direction.RIGHT, 0, 0)
    else:
        for i in range(len(data)):
            max_tiles = max(max_tiles, get_energized_tile_count(data, Direction.RIGHT, i, 0))
            max_tiles = max(max_tiles, get_energized_tile_count(data, Direction.LEFT, i, len(data[0]) - 1))

        for j in range(len(data[0])):
            max_tiles = max(max_tiles, get_energized_tile_count(data, Direction.DOWN, 0, j))
            max_tiles = max(max_tiles, get_energized_tile_count(data, Direction.UP, len(data) - 1, j))

    return max_tiles


def walk(tile_matrix: list[list[str]], direction: Direction, i: int = 0, j: int = 0, tiles: set = None) -> dict[tuple[int, int], set[Direction]]:
    if tiles is None:
        tiles = defaultdict(set)

    tiles[(i, j)].add(direction)

    while True:
        match tile_matrix[i][j]:
            case '\\':
                direction = direction.apply_backslash()
            case '/':
                direction = direction.apply_slash()
            case '-':
                if direction in (Direction.DOWN, Direction.UP):
                    tiles.update(walk(tile_matrix, Direction.LEFT, i, j, tiles))
                    direction = Direction.RIGHT
            case '|':
                if direction in (Direction.LEFT, Direction.RIGHT):
                    tiles.update(walk(tile_matrix, Direction.UP, i, j, tiles))
                    direction = Direction.DOWN

        i, j = direction.apply(i, j)

        if (i < 0 or j < 0 or i >= len(tile_matrix) or j >= len(tile_matrix[0])
                or direction in tiles[(i, j)]):
            break

        tiles[(i, j)].add(direction)

    return tiles


if __name__ == '__main__':
    print(solution(1))  # 7242
    print(solution(2))  # 7572
