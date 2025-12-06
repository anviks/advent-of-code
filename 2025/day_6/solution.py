from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", re.compile(r" +")), str)
lines = parse_file_content(file_path, ("\n",), str)


@stopwatch
def part1():
    # Remove empty strings
    problems = [[col for col in row if col] for row in data]
    problems = list(zip(*problems))
    result = 0

    # Join ('123', '45', '6', '*') into 123*45*6
    for problem in problems:
        result += eval(problem[-1].join(problem[:-1]))

    return result


@stopwatch
def part2():
    expression = ""
    active_op = ""

    # Read vertically, if digits are all spaces, insert +, otherwise insert number and last seen operator
    for *digits, op in zip(*lines):
        num = "".join(digits).strip()
        if not num:
            expression = expression[:-1] + "+"
            continue

        active_op = op.strip() or active_op
        expression += num + active_op

    return eval(expression[:-1])


if __name__ == "__main__":
    print(part1())  # 3785892992137 | 0.0065 seconds
    print(part2())  # 7669802156452 | 0.0045 seconds
