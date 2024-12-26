from utils_anviks import parse_file_content, parse_string, stopwatch

from coordinates import Cell
from grid import Grid

file = 'data.txt'
file0 = 'example.txt'
map1, instructions = parse_file_content(file, ('\n\n',), str)
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
    pass


if __name__ == '__main__':
    print(part1())  # 1398947   | 0.116 seconds
    print(part2())
