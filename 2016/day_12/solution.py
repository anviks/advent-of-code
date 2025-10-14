from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n", " "), str)


class Assembler:
    def __init__(self, instructions: list[list[str]], *, reg_c: int = 0) -> None:
        self.a = 0
        self.b = 0
        self.c = reg_c
        self.d = 0

        self.instructions = instructions
        self.pointer = 0

    def cpy(self, x: str, y: str):
        val = int(x) if x.isdigit() else getattr(self, x)
        setattr(self, y, val)

    def inc(self, x: str):
        setattr(self, x, getattr(self, x) + 1)

    def dec(self, x: str):
        setattr(self, x, getattr(self, x) - 1)

    def jnz(self, x: str, y: str):
        val = int(x) if x.isdigit() else getattr(self, x)
        if val != 0:
            self.pointer += int(y) - 1

    def execute(self):
        while self.pointer < len(self.instructions):
            cmd, *args = self.instructions[self.pointer]
            getattr(self, cmd)(*args)
            self.pointer += 1


@stopwatch
def part1():
    assembler = Assembler(data)
    assembler.execute()
    return assembler.a


@stopwatch
def part2():
    assembler = Assembler(data, reg_c=1)
    assembler.execute()
    return assembler.a


if __name__ == "__main__":
    print(part1())  # 318083    | 0.39 seconds
    print(part2())  # 9227737   | 11.3 seconds
