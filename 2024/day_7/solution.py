from utils_anviks import parse_file_content, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', ': ', ' '), int)


def is_computable(value: int, operands: list[int], concat: bool) -> bool:
    *ops, num = operands

    return (
        value % num == 0 and is_computable(value // num, ops, concat)
        or is_computable(value - num, ops, concat)
        or concat and str(value).endswith(str(num)) and is_computable(value // 10 ** len(str(num)), ops, concat)
    ) if ops else value == num


@stopwatch
def solution(part: int):
    return sum(
        value[0]
        for value, operands in data
        if is_computable(value[0], operands, concat=part == 2)
    )


if __name__ == '__main__':
    print(solution(1))  # 7885693428401
    print(solution(2))  # 348360680516005
