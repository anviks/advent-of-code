from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
import numpy as np

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n", " "), str)


@stopwatch
def solve():
    screen = np.zeros(shape=(6, 50), dtype=int)

    for cmd, *args in data:
        if cmd == "rect":
            cols, rows = map(int, args[0].split("x"))
            screen[:rows, :cols] = 1
        elif cmd == "rotate":
            direction, offset, _, delta = args
            offset = offset.split("=")[-1]
            if direction == "column":
                screen[:, int(offset)] = np.roll(screen[:, int(offset)], int(delta))
            else:
                screen[int(offset), :] = np.roll(screen[int(offset), :], int(delta))

    for row in screen:
        for col in row:
            print("#" if col else " ", end="")
        print()

    return np.sum(screen)


if __name__ == "__main__":
    print(solve())  # 110, ZJHRKCPLYJ   | 0.0017 seconds
