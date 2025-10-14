from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", " "), str)


class Interpreter:
    def __init__(self, instructions: list[list[str]], *, reg_c: int = 0) -> None:
        self.reg = {
            'a': 0,
            'b': 0,
            'c': reg_c,
            'd': 0,
        }

        self.instructions = instructions
        self.pointer = 0
    
    def get_value(self, x: str):
        return int(x) if x.isdigit() else self.reg[x]

    def cpy(self, x: str, y: str):
        val = self.get_value(x)
        self.reg[y] = val

    def inc(self, x: str):
        self.reg[x] += 1

    def dec(self, x: str):
        self.reg[x] -= 1

    def jnz(self, x: str, y: str):
        val = self.get_value(x)
        if val != 0:
            self.pointer += int(y) - 1

    def execute(self):
        while self.pointer < len(self.instructions):
            cmd, *args = self.instructions[self.pointer]
            getattr(self, cmd)(*args)
            self.pointer += 1


@stopwatch
def part1():
    interpreter = Interpreter(data)
    interpreter.execute()
    return interpreter.reg['a']


@stopwatch
def part2():
    interpreter = Interpreter(data, reg_c=1)
    interpreter.execute()
    return interpreter.reg['a']


if __name__ == "__main__":
    print(part1())  # 318083    | 0.39 seconds
    print(part2())  # 9227737   | 11.3 seconds
