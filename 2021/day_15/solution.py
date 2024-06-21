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
        nodes = [(0, id_, 0j)]
        target = max(self.grid, key=lambda c: (c.real, c.imag))
        distances = {0j: self.grid[0j]}

        while nodes:
            risk, _, coord = pop(nodes)
            
            if coord == target:
                return risk

            for neighbour in self.get_neighbours(coord):
                new_risk = self.grid[neighbour]
                if neighbour not in distances or new_risk < distances[neighbour]:
                    distances[neighbour] = new_risk
                    id_ += 1
                    push(nodes, (risk + new_risk, id_, neighbour))


    @stopwatch
    def part2(self) -> int:
        id_ = 0
        # risk sum, id, coord, visited
        nodes = [(0, id_, 0j)]
        target = max(self.grid, key=lambda c: (c.real, c.imag))
        height, width = int(target.real) + 1, int(target.imag) + 1
        target = complex(height * 5 - 1, width * 5 - 1)
        distances = {0j: self.grid[0j]}

        while nodes:
            risk, _, coord = pop(nodes)
            if coord == target:
                return int(risk)

            for neighbour in [coord + 1, coord - 1, coord + 1j, coord - 1j]:
                if 0 > neighbour.real >= target.real or 0 > neighbour.imag >= target.imag:
                    continue
                
                shift = neighbour.real // height + neighbour.imag // width
                bound_neighbour = complex(neighbour.real % height, neighbour.imag % width)
                new_risk = (self.grid[bound_neighbour] + shift) % 9 or 9
                
                if neighbour not in distances or new_risk < distances[neighbour]:
                    distances[neighbour] = new_risk
                    id_ += 1
                    push(nodes, (risk + new_risk, id_, neighbour))


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 458
    print(solver.part2())  # 2800


if __name__ == '__main__':
    main()
