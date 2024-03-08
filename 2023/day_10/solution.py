from enum import Enum

from utils_anviks import read_file, stopwatch


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


def make_move(pipe: str, previous_move: Direction, i: int, j: int) -> tuple[int, int, Direction]:
    new_direction = previous_move

    # If the pipe is straight, we can move in the same direction as before.
    match pipe:
        case "L":
            if previous_move == Direction.DOWN:
                new_direction = Direction.RIGHT
            else:
                new_direction = Direction.UP
        case "J":
            if previous_move == Direction.RIGHT:
                new_direction = Direction.UP
            else:
                new_direction = Direction.LEFT
        case "7":
            if previous_move == Direction.RIGHT:
                new_direction = Direction.DOWN
            else:
                new_direction = Direction.LEFT
        case "F":
            if previous_move == Direction.UP:
                new_direction = Direction.RIGHT
            else:
                new_direction = Direction.DOWN

    return new_direction.apply(i, j) + (new_direction,)


@read_file(sep2="")
@stopwatch
def solution(data: list[list[str]], part: int):
    coords = set()
    i, j = find_starting_point(data)
    coords.add((i, j))
    prev_move = None

    # ("|", "-", "L", "J", "7", "F")

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

    with open("modified.txt", "w") as f:
        f.write("\n".join("".join(line) for line in data))

    return steps // 2 if part == 1 else enclosed_tiles


if __name__ == '__main__':
    print(solution(1))  # 6931
    print(solution(2))  # 357



    # from matplotlib.path import Path
    #
    # ans_2 = 0
    #
    # p = Path(list(coords))
    # print()
    # for i in range(len(data)):
    #     for j in range(len(data[0])):
    #         if (i, j) in coords:
    #             continue
    #         if p.contains_point((i, j)):
    #             ans_2 += 1
    #
    # print(ans_2)
