import sys

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
    dfs(start, set(), map_, end)
    return best


direction_to_tile = {1: 'v', -1: '^', 1j: '>', -1j: '<'}


best = 0

def dfs(location: complex, visited: set, map_, end):
    global best
    if location == end:
        best = max(best, len(visited))

    for direction in 1, -1, 1j, -1j:
        next_loc = location + direction
        next_tile = map_.get(next_loc, '#')
        if next_loc not in visited and (next_tile != '#'):
            visited.add(next_loc)
            dfs(next_loc, visited, map_, end)
            visited.remove(next_loc)



if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(solution(1))  # 2030  |  3.5s  |  0.38s
    print(solution(2))
