from collections import deque
from functools import cache
from itertools import product

from utils_anviks import parse_file_content, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), str)

directions = {
    (1, 0): 'v',
    (-1, 0): '^',
    (0, 1): '>',
    (0, -1): '<',
}


def dir_keypad_to_press(res: str):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    pressed = []
    keys = '<v>^A'
    idx = 4

    for to_press in res:
        target = keys.index(to_press)
        while idx != target:
            if idx > target:
                if idx > target + idx % 3:
                    idx -= 2
                    pressed.append('v')
                else:
                    idx -= 1
                    pressed.append('<')
            else:
                if target > idx + target % 3 and idx != 0:
                    idx += 2
                    pressed.append('^')
                else:
                    idx += 1
                    pressed.append('>')
        pressed.append('A')

    print(''.join(pressed))
    return ''.join(pressed)


dir_cache = {}


@cache
def keypad_to_press(res: str, depth: int, is_dir_keypad=False):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    possibilities = []
    if is_dir_keypad:
        keys = Grid([
            [None, '^', 'A'],
            ['<', 'v', '>'],
        ])
        start = Cell(0, 2)
    else:
        keys = Grid([
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [None, '0', 'A'],
        ])
        start = Cell(3, 2)

    for to_press in res:
        target = keys.find_first(to_press)
        best = start.manhattan_distance(target)
        todo = deque([(start, '')])
        possibilities.append([])
        while todo:
            cell, path = todo.popleft()

            if len(path) > best:
                continue

            if cell == target:
                if depth == 0:
                    possibilities[-1].append(path + 'A')
                else:
                    sub_poss = keypad_to_press(path + 'A', depth - 1, True)
                    shortest = min(map(len, sub_poss))
                    for poss in sub_poss:
                        if len(poss) == shortest:
                            possibilities[-1].append(poss)
                continue

            for nb_dir in keys.neighbour_directions(cell, 'cardinal'):
                nb = cell + nb_dir
                if keys[nb] is None:
                    continue
                next_key = directions[nb_dir]
                if next_key in path and path[-1] != next_key:
                    continue
                todo.append((nb, path + next_key))
        start = target

    str_possibilities = []

    for poss in product(*possibilities):
        str_possibilities.append(''.join(poss))

    return str_possibilities


@stopwatch
def part1():
    acc = 0
    for code in data:
        result = keypad_to_press(code, 2)
        aaaa = min(map(len, result))
        acc += aaaa * int(code[:-1])
        print(aaaa, '*', int(code[:-1]))
    return acc


# def part2():
#     acc = 0
#     for code in data:
#         result = keypad_to_press(code, 25)
#         aaaa = min(map(len, result))
#         acc += aaaa * int(code[:-1])
#         print(aaaa, '*', int(code[:-1]))
#     return acc


if __name__ == '__main__':
    print(part1())  # 278748    | 0.013 seconds
    # print(part2())
