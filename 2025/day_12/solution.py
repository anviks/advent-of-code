from functools import cache, wraps
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch, parse_string
from concurrent.futures import ThreadPoolExecutor, TimeoutError

type Shape = frozenset[tuple[int, int]]
type Board = list[list[bool]]

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file0
*shapes, regions = parse_file_content(file_path, ("\n\n",), str)
regions = parse_string(regions, ("\n", ": ", " "), str)[:-1]

shape_coords = []
for shape in shapes:
    rows = shape.split("\n")[1:]
    coord_set = set()

    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            if col == "#":
                coord_set.add((i, j))

    shape_coords.append(frozenset(coord_set))


def print_shape(shape: Shape):
    max_i = max(i for i, j in shape)
    max_j = max(j for i, j in shape)
    for i in range(max_i + 1):
        row = ""
        for j in range(max_j + 1):
            if (i, j) in shape:
                row += "#"
            else:
                row += "."
        print(row)
    print()


def timeout(seconds=1, default=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)
                try:
                    return future.result(timeout=seconds)
                except TimeoutError:
                    return default
        return wrapper
    return decorator


@cache
def normalize(cells):
    minx = min(x for x, _ in cells)
    miny = min(y for _, y in cells)
    return frozenset((x - minx, y - miny) for x, y in cells)


@cache
def rotate(shape: Shape) -> Shape:
    return normalize(frozenset({(y, -x) for x, y in shape}))


@cache
def flip(shape: Shape) -> Shape:
    return normalize(frozenset({(-x, y) for x, y in shape}))


@cache
def all_variants(shape: Shape):
    variants: set[Shape] = set()
    cur = shape
    for _ in range(4):
        cur = rotate(cur)
        variants.add(cur)
        variants.add(flip(cur))
    return list(variants)


def can_place(board: Board, shape: Shape, x0: int, y0: int):
    H, W = len(board), len(board[0])
    for x, y in shape:
        x += x0
        y += y0
        if x < 0 or y < 0 or x >= H or y >= W:
            return False
        if board[x][y]:
            return False
    return True


def place(board: Board, shape: Shape, x0: int, y0: int, value=True):
    for x, y in shape:
        board[x + x0][y + y0] = value


# @timeout(1, default=False)
def solve(board: Board, shapes: list[list[Shape]], i=0):
    if i == len(shapes):
        return True

    H, W = len(board), len(board[0])

    for shape in shapes[i]:
        maxx = max(x for x, _ in shape)
        maxy = max(y for _, y in shape)

        for x in range(H - maxy):
            for y in range(W - maxx):
                if can_place(board, shape, x, y):
                    place(board, shape, x, y, True)
                    if solve(board, shapes, i + 1):
                        return True
                    place(board, shape, x, y, False)

    return False


@stopwatch
def part1():
    total = 0

    for (size,), counts in regions:
        W, H = map(int, size.split("x"))
        board = [[False] * W for _ in range(H)]
        shapes: list[list[Shape]] = []

        for i, count in enumerate(counts):
            count = int(count)
            if count == 0:
                continue

            for _ in range(count):
                shapes.append(all_variants(shape_coords[i]))

        result = solve(board, shapes)
        print(result)
        total += result

    return total



@stopwatch
def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
