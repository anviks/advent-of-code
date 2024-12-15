from enum import Enum

from utils_anviks import parse_file_content, stopwatch


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    def apply(self, i: int, j: int) -> tuple[int, int]:
        di, dj = self.value
        return i + di, j + dj


def find_starting_point(data: list[list[str]]):
    for i, row in enumerate(data):
        if "S" in row:
            return i, row.index("S")


DIRECTION_MAP = {
    "L": {Direction.DOWN: Direction.RIGHT, Direction.LEFT: Direction.UP},
    "J": {Direction.RIGHT: Direction.UP, Direction.DOWN: Direction.LEFT},
    "7": {Direction.RIGHT: Direction.DOWN, Direction.UP: Direction.LEFT},
    "F": {Direction.UP: Direction.RIGHT, Direction.LEFT: Direction.DOWN},
}
def make_move(pipe: str, previous_move: Direction, i: int, j: int) -> tuple[int, int, Direction]:
    # If the pipe is straight, we can move in the same direction as before.
    new_direction = DIRECTION_MAP.get(pipe, {}).get(previous_move, previous_move)
    return new_direction.apply(i, j) + (new_direction,)


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n', ''), str)
    i, j = find_starting_point(data)
    coords = {(i, j)}
    prev_move = None

    if data[i - 1][j] in ("|", "7", "F"):
        i -= 1
        prev_move = Direction.UP
    elif data[i + 1][j] in ("|", "L", "J"):
        i += 1
        prev_move = Direction.DOWN
    elif data[i][j - 1] in ("-", "L", "F"):
        j -= 1
        prev_move = Direction.LEFT
    elif data[i][j + 1] in ("-", "7", "J"):
        j += 1
        prev_move = Direction.RIGHT

    steps = 1
    coords.add((i, j))

    while data[i][j] != "S":
        pipe = data[i][j]
        i, j, prev_move = make_move(pipe, prev_move, i, j)
        coords.add((i, j))
        steps += 1

    if part == 1:
        return steps // 2

    enclosed_tiles = 0

    for i, row in enumerate(data):
        enclosed = False
        for j, char in enumerate(row):
            if (i, j) not in coords:
                data[i][j] = "X"
                char = "X"

            if char in "|LJ":
                enclosed = not enclosed
            elif enclosed and char == "X":
                enclosed_tiles += 1
                data[i][j] = "O"

    return enclosed_tiles


def draw_grid(data: list[list[str]]):
    with open("grid.txt", "w") as f:
        f.write("\n".join("".join(line) for line in data))


if __name__ == '__main__':
    print(solution(1))  # 6931  | 0.018 seconds
    print(solution(2))  # 357   | 0.017 seconds
