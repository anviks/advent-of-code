from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n", ""), str)


class KeyPad:
    def __init__(self, keypad_design: list[str], row: int, col: int) -> None:
        self.design = keypad_design
        self.row = row
        self.col = col

    def U(self):
        if self.design[self.row - 1][self.col] != " ":
            self.row -= 1

    def D(self):
        if self.design[self.row + 1][self.col] != " ":
            self.row += 1

    def L(self):
        if self.design[self.row][self.col - 1] != " ":
            self.col -= 1

    def R(self):
        if self.design[self.row][self.col + 1] != " ":
            self.col += 1

    def current(self):
        return self.design[self.row][self.col]


def solve(keypad: KeyPad):
    code = ""

    for row in data:
        for char in row:
            getattr(keypad, char)()

        code += str(keypad.current())

    return code


@stopwatch
def part1():
    keypad = KeyPad(["     ", " 123 ", " 456 ", " 789 ", "     "], 2, 2)
    return solve(keypad)


@stopwatch
def part2():
    keypad = KeyPad(
        ["       ", "   1   ", "  234  ", " 56789 ", "  ABC  ", "   D   ", "       "],
        3,
        1,
    )
    return solve(keypad)


if __name__ == "__main__":
    print(part1())  # 92435 | 0.00036 seconds
    print(part2())  # C1A88 | 0.00036 seconds
