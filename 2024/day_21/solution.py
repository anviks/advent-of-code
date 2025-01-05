from functools import cache

from utils_anviks import parse_file_content, stopwatch, Cell, Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), str)

dir_pad = Grid([
    [None, '^', 'A'],
    ['<', 'v', '>'],
])

num_pad = Grid([
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
])


@cache
def find_path(start: str, end: str):
    keypad = dir_pad if start in '<v^>' or end in '<v^>' else num_pad
    c_start = keypad.find_first(start)
    c_end = keypad.find_first(end)
    diff = c_end - c_start
    y_move = diff.row * 'v' + -diff.row * '^'
    x_move = diff.column * '>' + -diff.column * '<'

    bad = keypad.find_first(None) - c_start
    prefer_y = (diff.column > 0 or bad == Cell(0, diff.column)) and bad != Cell(diff.row, 0)
    result = y_move + x_move if prefer_y else x_move + y_move

    return result + 'A'


@cache
def keypress_length(code: str, depth: int):
    if depth == 0:
        return len(code)
    total = 0
    for i, char in enumerate(code):
        total += keypress_length(find_path(code[i - 1], char), depth - 1)
    return total


def solve(depth: int):
    acc = 0
    for code in data:
        result = keypress_length(code, depth)
        acc += result * int(code[:-1])
    return acc


@stopwatch
def part1():
    return solve(3)


@stopwatch
def part2():
    return solve(26)


if __name__ == '__main__':
    print(part1())  # 278748            | 0.00027 seconds
    print(part2())  # 337744744231414   | 0.00029 seconds
