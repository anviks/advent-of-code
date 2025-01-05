from collections import deque

from utils_anviks import parse_file_content, stopwatch, Grid

file = 'data.txt'
file0 = 'example.txt'
data = Grid(parse_file_content(file, ('\n', ''), int))


@stopwatch
def solution(part: int):
    zero_indices = data.find(0)
    result = 0

    for zero_coord in zero_indices:
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

            for nb in data.neighbours(current, 'cardinal'):
                if data[nb] == data[current] + 1:
                    d.append(nb)

    return result


if __name__ == '__main__':
    print(solution(1))  # 593   | 0.034 seconds
    print(solution(2))  # 1192  | 0.048 seconds
