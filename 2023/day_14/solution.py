from typing import TypeVar

from utils_anviks import parse_file_content, stopwatch

from grid import Grid

_T = TypeVar("_T")


@stopwatch
def solution(part: int):
    """
    Solution for the day 14 problem.

    For part 1, return the total load of the rocks after 1 tilt to the north.
    For part 2, return the total load of the rocks after 1_000_000_000 cycles of tilting (north, west, south, east).
    :param part: The part of the problem to solve.
    :return: The solution for the given part.
    """
    data = Grid(parse_file_content('data.txt', ('\n', ''), str))

    if part == 1:
        tilt_north(data)

        return calculate_total_load(data)
    else:
        total_loads = []

        for i in range(165):
            tilt_cycle(data)
            total_loads.append(calculate_total_load(data))

        cycle = find_cycle(total_loads)

        return cycle[(1_000_000_000 - len(total_loads) - 1) % len(cycle)]


def calculate_total_load(rocks: Grid[str]) -> int:
    """
    Calculate the total load of the rocks.

    The load of one O-rock is equal to the number of rows below it + 1,
    meaning that if there are 10 rows of rocks, a rock in the 1st row (from the top) has a load of 10
    and a rock in the 10th row has a load of 1.
    :param rocks: The rocks.
    :return: The total load of the rocks.
    """
    load = 0

    for i, line in enumerate(rocks.rows):
        load += (rocks.height - i) * line.count('O')

    return load


def _find_cycle_helper(sequence: list[_T], window_size: int) -> list[_T] | None:
    window_1 = sequence[-window_size:]
    window_2 = sequence[-window_size * 2: -window_size]
    return window_1 if window_1 == window_2 else None


def find_cycle(sequence: list[_T]) -> list[_T] | None:
    for i in range(2, len(sequence) // 2 + 1):
        if result := _find_cycle_helper(sequence, i):
            return result

    return None


def tilt_cycle(rocks: Grid[str]) -> None:
    for _ in range(4):
        tilt_north(rocks)
        rocks.rotate_clockwise()


def tilt_north(rocks: Grid[str]) -> None:
    for i in range(rocks.width):
        obstacle_index = -1
        for j in range(rocks.height):
            rock = rocks.grid[j][i]

            match rock:
                case 'O':
                    if obstacle_index + 1 == j:
                        obstacle_index += 1
                    else:
                        rocks.grid[obstacle_index + 1][i] = 'O'
                        obstacle_index += 1
                        rocks.grid[j][i] = '.'
                case '#':
                    obstacle_index = j


if __name__ == '__main__':
    print(solution(1))  # 107142    | 0.004 seconds
    print(solution(2))  # 104815    | 0.69 seconds
