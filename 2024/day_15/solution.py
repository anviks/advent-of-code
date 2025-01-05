from utils_anviks import parse_file_content, parse_string, stopwatch, Grid, Cell

file = 'data.txt'
file0 = 'example.txt'
map1, instructions = parse_file_content(file, ('\n\n',), str)
map2 = (map1
        .replace('#', '##')
        .replace('O', '[]')
        .replace('.', '..')
        .replace('@', '@.'))
moves = instructions.replace('\n', '')
directions = {'^': -1, 'v': 1, '<': -1j, '>': 1j}


def solve(grid: Grid[str], can_move_func, move_func, box_symbol: str):
    robot = grid.find_first('@')
    for arrow in moves:
        direction = directions[arrow]
        if can_move_func(robot, direction):
            move_func(robot, direction)
            robot += direction

    return sum(box.row * 100 + box.column for box in grid.find(box_symbol))


@stopwatch
def part1():
    def can_move(from_: Cell, d: complex):
        new = from_ + d
        new_val = grid[new]
        if new_val == 'O':
            return can_move(new, d)
        return new_val == '.'

    def move(from_: Cell, d: complex):
        to = from_ + d
        if grid[to] == 'O':
            move(to, d)
        grid[to], grid[from_] = grid[from_], grid[to]

    grid = Grid(parse_string(map1, ('\n', ''), str))
    return solve(grid, can_move, move, 'O')


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

        if (d == -1j and to_val == ']'
                or d == 1j and to_val == '['):
            move(to + d, d)
            grid[to + d], grid[to], grid[from_] = grid[to], grid[from_], grid[to + d]
        elif d.real:
            move(to, d)
            if to_val == ']':
                move(to.left, d)
            elif to_val == '[':
                move(to.right, d)
            grid[to], grid[from_] = grid[from_], grid[to]

    grid = Grid(parse_string(map2, ('\n', ''), str))
    return solve(grid, can_move, move, '[')


if __name__ == '__main__':
    print(part1())  # 1398947   | 0.095 seconds
    print(part2())  # 1397393   | 0.110 seconds
