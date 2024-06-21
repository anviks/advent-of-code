from collections import deque
from typing import Generator
from heapq import heappop as pop, heappush as push

from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        data = parse_file_content(input_file_name, ('\n', ''), int)
        self.grid: dict[complex, int] = {complex(i, j): square
                                         for i, row in enumerate(data)
                                         for j, square in enumerate(row)}

    def get_neighbours(self, coordinate: complex) -> Generator[complex, None, None]:
        for neighbour in [coordinate + 1, coordinate - 1, coordinate + 1j, coordinate - 1j]:
            if neighbour in self.grid:
                yield neighbour

    @stopwatch
    def part1(self) -> int:
        id_ = 0
        # risk sum, id, coord, visited
        d = [(0, id_, 0j)]
        target = max(self.grid, key=lambda c: (c.real, c.imag))
        distances = {0j: self.grid[0j]}

        while d:
            risk, _, coord = pop(d)
            
            if coord == target:
                return risk

            for n in self.get_neighbours(coord):
                new_risk = self.grid[n]
                if n not in distances or new_risk < distances[n]:
                    distances[n] = new_risk
                    id_ += 1
                    push(d, (risk + new_risk, id_, n))


    @stopwatch
    def part2(self) -> int:
        id_ = 0
        # risk sum, id, coord, visited
        d = [(0, id_, 0j)]
        target = max(self.grid, key=lambda c: (c.real, c.imag))
        height, width = int(target.real) + 1, int(target.imag) + 1
        target = complex(height * 5 - 1, width * 5 - 1)
        distances = {0j: self.grid[0j]}

        while d:
            risk, _, coord = pop(d)
            if coord == target:
                return int(risk)

            for n in [coord + 1, coord - 1, coord + 1j, coord - 1j]:
                if 0 > n.real >= target.real or 0 > n.imag >= target.imag:
                    continue
                
                shift = n.real // height + n.imag // width
                bound_n = complex(n.real % height, n.imag % width)
                new_risk = (self.grid[bound_n] + shift) % 9 or 9
                
                if n not in distances or new_risk < distances[n]:
                    distances[n] = new_risk
                    id_ += 1
                    push(d, (risk + new_risk, id_, n))


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 458
    print(solver.part2())  # 2800


if __name__ == '__main__':
    main()
