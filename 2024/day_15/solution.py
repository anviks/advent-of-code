from utils_anviks import parse_file_content, parse_string, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
map1, instructions = parse_file_content(file, ('\n\n',), str)
map2 = (map1
        .replace('#', '##')
        .replace('O', '[]')
        .replace('.', '..')
        .replace('@', '@.'))
moves = instructions.replace('\n', '')
comp_moves = []
count, prev = 1, moves[0]
for i in range(1, len(moves)):
    if moves[i] == prev:
        count += 1
    else:
        comp_moves.append((count, prev))
        count, prev = 1, moves[i]
comp_moves.append((count, prev))
directions = {'^': -1, 'v': 1, '<': -1j, '>': 1j}


@stopwatch
def part1():
    grid = Grid(parse_string(map1, ('\n', ''), str))
    robot = grid.find_first('@')
    for n, arrow in comp_moves:
        direction = directions[arrow]
        peek = robot + direction
        free, boxes = 0, 0
        while (val := grid[peek]) != '#' and free < n:
            if val == '.':
                free += 1
            elif val == 'O':
                boxes += 1
            peek += direction
        if free > 0:
            grid[robot] = '.'
            grid[robot:robot + direction * (free + boxes)] = '.'
            robot = robot + direction * free
            if boxes:
                grid[robot:robot + direction * boxes] = 'O'
            grid[robot] = '@'

    return sum(box.row * 100 + box.column for box in grid.find('O'))


@stopwatch
def part2():
    def can_move(from_: Cell, d: complex):
        new = from_ + d
        new_val = grid[new]
        if new_val in '[]':
            if d.imag:
                return can_move(new + d, d)
            else:
                if new_val == '[':
                    pair = new.right
                else:
                    pair = new.left
                return can_move(new, d) and can_move(pair, d)

        return new_val == '.'

    def move(from_: Cell, d: complex):
        to = from_ + d
        to_val = grid[to]

        if to_val == '.':
            grid[to], grid[from_] = grid[from_], grid[to]
            return

        if to_val == '#':
            return

        if (d == -1j and to_val == ']'
                or d == 1j and to_val == '['):
            move(to + d, d)
            grid[to + d], grid[to], grid[from_] = grid[to], grid[from_], grid[to + d]
        elif d.real:
            if to_val == ']':
                move(to, d)
                move(to.left, d)
                grid[to], grid[from_] = grid[from_], grid[to]
            elif to_val == '[':
                move(to, d)
                move(to.right, d)
                grid[to], grid[from_] = grid[from_], grid[to]


    grid = Grid(parse_string(map2, ('\n', ''), str))
    robot = grid.find_first('@')
    for arrow in moves:
        direction = directions[arrow]
        if can_move(robot, direction):
            move(robot, direction)
            robot += direction

    return sum(box.row * 100 + box.column for box in grid.find('['))


if __name__ == '__main__':
    print(part1())  # 1398947   | 0.116 seconds
    print(part2())  # 1397393   | 0.144 seconds
