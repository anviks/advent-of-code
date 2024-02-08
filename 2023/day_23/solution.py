from utils_anviks import read_data, stopwatch
from collections import deque


@read_data('data.txt', auto_annotate=True)
@stopwatch
def solution(data: list[str], part: int):
    map_ = {}
    start = None
    end = None

    for i in range(len(data)):
        for j in range(len(data[0])):
            coord = i + j * 1j
            tile = data[i][j]
            map_[coord] = tile

            if i == 0 and tile == '.':
                start = coord
            elif i == len(data) - 1 and tile == '.':
                end = coord

    direction_to_tile = {1: 'v', -1: '^', 1j: '>', -1j: '<'}
    paths = deque([(start, 0, set())])
    path_steps = []

    while paths:
        loc_steps, steps, visited = paths.popleft()

        if loc_steps == end:
            path_steps.append(steps)
            continue

        to_be_added = []

        for direction in 1, -1, 1j, -1j:
            next_loc = loc_steps + direction
            next_tile = map_.get(next_loc, '#')
            if next_loc not in visited and (next_tile == '.' or direction_to_tile[direction] == next_tile):
                to_be_added.append((next_loc, steps + 1))

        for i in range(len(to_be_added)):
            loc, steps = to_be_added[i]

            if i == len(to_be_added) - 1:
                visited.add(loc)
                paths.append((loc, steps, visited))
            else:
                copy = visited.copy()
                copy.add(loc)
                paths.append((loc, steps, copy))


    return max(path_steps)


if __name__ == '__main__':
    print(solution(1))  # 2030  |  3.5s  |  0.38s
    print(solution(2))
