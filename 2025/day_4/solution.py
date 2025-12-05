from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", ""), str)


def get_surrounding_rolls(row: int, col: int) -> list[tuple[int, int]]:
    rolls = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            r, c = row + i, col + j
            if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == "@":
                rolls.append((r, c))
    return rolls


@stopwatch
def part1():
    accessible = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            accessible += data[i][j] == "@" and len(get_surrounding_rolls(i, j)) < 4

    return accessible


@stopwatch
def part2():
    roll_coords = set()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                roll_coords.add((i, j))

    total_removed = 0

    while True:
        temp_removed = 0

        for roll in roll_coords.copy():
            nbs = 0
            for nb in get_surrounding_rolls(*roll):
                if nb in roll_coords:
                    nbs += 1
            if nbs <= 3:
                roll_coords.remove(roll)
                temp_removed += 1

        # Break if none can be removed
        if temp_removed == 0:
            break

        total_removed += temp_removed

    return total_removed


if __name__ == "__main__":
    print(part1())  # 1491  | 0.023 seconds
    print(part2())  # 8722  | 0.432 seconds
