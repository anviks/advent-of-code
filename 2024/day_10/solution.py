from collections import deque

from utils_anviks import parse_file_content, stopwatch
import numpy as np

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), int)
data = np.array(data)


@stopwatch
def solution(part: int):
    indices = np.where(data == 0)
    result = 0

    for zero_coord in zip(*indices):
        visited = set()
        d = deque([zero_coord])
        while len(d):
            current = d.popleft()

            if part == 1:
                if (zero_coord, current) in visited:
                    continue
                visited.add((zero_coord, current))

            if data[current] == 9:
                result += 1
                continue

            for nb in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_coord = (current[0] + nb[0], current[1] + nb[1])
                if all(0 <= index < length for index, length in zip(new_coord, data.shape)) and data[new_coord] == data[current] + 1:
                    d.append(new_coord)

    return result


if __name__ == '__main__':
    print(solution(1))  # 593
    print(solution(2))  # 1192
