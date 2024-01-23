from enum import Enum

from utils_anviks.decorators import read_data, stopwatch


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4



@read_data
@stopwatch
def solution(data: list[str], part: int):
    i = j = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                break
        else:
            continue
        break

    steps = 0
    prev_move = None

    # ("|", "-", "L", "J", "7", "F")

    if data[i - 1][j] in ("|", "7", "F"):
        i -= 1
        prev_move = Direction.UP
    if data[i + 1][j] in ("|", "L", "J"):
        i += 1
        prev_move = Direction.DOWN
    if data[i][j - 1] in ("-", "L", "F"):
        j -= 1
        prev_move = Direction.LEFT
    if data[i][j + 1] in ("-", "7", "J"):
        j += 1
        prev_move = Direction.RIGHT

    steps += 1

    while data[i][j] != "S":
        pipe = data[i][j]

        if pipe == "|":
            if prev_move == Direction.DOWN:
                i += 1
            else:
                i -= 1
        elif pipe == "-":
            if prev_move == Direction.RIGHT:
                j += 1
            else:
                j -= 1
        elif pipe == "L":
            if prev_move == Direction.DOWN:
                j += 1
                prev_move = Direction.RIGHT
            else:
                i -= 1
                prev_move = Direction.UP
        elif pipe == "J":
            if prev_move == Direction.RIGHT:
                i -= 1
                prev_move = Direction.UP
            else:
                j -= 1
                prev_move = Direction.LEFT
        elif pipe == "7":
            if prev_move == Direction.RIGHT:
                i += 1
                prev_move = Direction.DOWN
            else:
                j -= 1
                prev_move = Direction.LEFT
        elif pipe == "F":
            if prev_move == Direction.UP:
                j += 1
                prev_move = Direction.RIGHT
            else:
                i += 1
                prev_move = Direction.DOWN

        steps += 1

    return steps / 2


if __name__ == '__main__':
    print()
    print(solution(1))
    print(solution(2))
