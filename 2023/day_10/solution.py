from utils_anviks import Cell, Grid, parse_file_content, stopwatch

data = parse_file_content('data.txt', ('\n', ''), str)
DIRECTION_MAP = {
    "L": {1: 1j, -1j: -1},
    "J": {1j: -1, 1: -1j},
    "7": {1j: 1, -1: -1j},
    "F": {-1: 1j, -1j: 1},
}


def make_move(pipe: str, previous_move: complex, cell: Cell) -> tuple[Cell, complex]:
    # If the pipe is straight, we can move in the same direction as before.
    new_direction = DIRECTION_MAP.get(pipe, {}).get(previous_move, previous_move)
    return cell + new_direction, new_direction


@stopwatch
def solution(part: int):
    grid = Grid(data)
    cell = grid.find_first('S')
    coords = {cell}
    prev_move = None

    if grid[cell.up] in ("|", "7", "F"):
        cell = cell.up
        prev_move = -1
    elif grid[cell.down] in ("|", "L", "J"):
        cell = cell.down
        prev_move = 1
    elif grid[cell.left] in ("-", "L", "F"):
        cell = cell.left
        prev_move = -1j
    elif grid[cell.right] in ("-", "7", "J"):
        cell = cell.right
        prev_move = 1j

    steps = 1
    coords.add(cell)

    while grid[cell] != "S":
        pipe = grid[cell]
        cell, prev_move = make_move(pipe, prev_move, cell)
        coords.add(cell)
        steps += 1

    if part == 1:
        return steps // 2

    enclosed_tiles = 0

    for i, row in enumerate(data):
        enclosed = False
        for j, char in enumerate(row):
            cell = Cell(i, j)
            if cell not in coords:
                grid[cell] = "X"
                char = "X"

            if char in "|LJ":
                enclosed = not enclosed
            elif enclosed and char == "X":
                enclosed_tiles += 1
                grid[cell] = "O"

    return enclosed_tiles


def draw_grid(grid: Grid[str]):
    with open("grid.txt", "w") as f:
        f.write(grid.join_to_str())


if __name__ == '__main__':
    print(solution(1))  # 6931  | 0.024 seconds
    print(solution(2))  # 357   | 0.031 seconds
