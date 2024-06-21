import sys

from utils_anviks import parse_file_content, stopwatch

DIRECTION_TO_TILE = {1: 'v', -1: '^', 1j: '>', -1j: '<'}


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n',), str)
    grid = {}
    visited = set()
    start = None
    end = None
    edges = {}
    weighed_edges = {}

    # Create a grid from the data
    for i in range(len(data)):
        for j in range(len(data[0])):
            coord = i + j * 1j
            tile = data[i][j]

            # No need to store obstacles
            if tile == '#':
                continue

            grid[coord] = tile

            if i == 0 and tile == '.':
                start = coord
            elif i == len(data) - 1 and tile == '.':
                end = coord

    for point in grid:
        neighbours = []

        for direction in (1, -1, 1j, -1j):
            if point + direction in grid:
                neighbours.append(point + direction)

        edges[point] = neighbours

    for point in grid:
        weighed_edges[point] = [collapse(edges, point, next_p) for next_p in edges[point]]

    if part == 1:
        return grid_walk(start, end, visited, grid)
    else:
        return graph_walk(start, end, visited, weighed_edges)


def collapse(edges, current_point, next_point, distance=1):
    """Collapse edges into a single node if it has exactly 2 neighbors."""
    while len(neighbours := edges[next_point]) == 2:
        previous_point = current_point
        current_point = next_point
        # Get the neighbour, that isn't the previous node
        next_point = neighbours[neighbours[0] == previous_point]
        distance += 1

    return next_point, distance


def grid_walk(location: complex, end: complex, visited: set, grid: dict[complex, str], best: int = 0):
    """Walk the grid and return the longest path, considering the direction restrictions (<, >, ^, v)."""
    if location == end:
        return max(best, len(visited))

    for direction in 1, -1, 1j, -1j:
        next_loc = location + direction
        next_tile = grid.get(next_loc, '#')

        if next_loc in visited:
            continue

        if next_tile in ('.', DIRECTION_TO_TILE[direction]):
            visited.add(next_loc)
            best = grid_walk(next_loc, end, visited, grid, best)
            visited.remove(next_loc)

    return best


def graph_walk(location: complex, end: complex, visited: set, edges: dict[complex, list], best: int = 0, weight_sum: int = 0):
    """Walk the graph and return the longest path, ignoring the direction restrictions (<, >, ^, v)."""
    if location == end:
        return max(best, weight_sum)

    next_edges = edges[location]

    for loc, steps in next_edges:
        if loc in visited:
            continue

        visited.add(loc)
        best = graph_walk(loc, end, visited, edges, best, weight_sum + steps)
        visited.remove(loc)

    return best


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(solution(1))  # 2030
    print(solution(2))  # 6390
