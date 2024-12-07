from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ': ', ' '), int)


def is_computable(value: int, operands: list[int], concat: bool) -> bool:
    *ops, num = operands

    if not ops:
        return value == num

    if value % num == 0 and is_computable(value // num, ops, concat):
        return True

    if is_computable(value - num, ops, concat):
        return True

    if concat and str(value).endswith(str(num)) and is_computable(value // 10 ** len(str(num)), ops, concat):
        return True

    return False


@stopwatch
def solution(part: int):
    acc = 0
    for value, operands in data:
        if is_computable(value[0], operands, concat=part == 2):
            acc += value[0]
    return acc


if __name__ == '__main__':
    print(solution(1))  # 7885693428401
    print(solution(2))  # 348360680516005
