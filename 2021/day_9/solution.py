import math
from typing import Generator

from utils_anviks import stopwatch, parse_file_content


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        data = parse_file_content(input_file_name, sep2='', _class=int)
        self.grid = {complex(i, j): square
                     for i, row in enumerate(data)
                     for j, square in enumerate(row)}
        self.low_points = [point for point in self.grid if self.is_low_point(point)]
    
    @stopwatch    
    def part1(self) -> int:
        risk_level_sum = sum(self.grid[point] + 1 for point in self.low_points)
        return risk_level_sum
    
    @stopwatch
    def part2(self) -> int:
        return math.prod(sorted((self.count_basins(point) for point in self.low_points), reverse=True)[:3])

    def count_basins(self, low_point_coord: complex) -> int:
        if self.grid[low_point_coord] == 9:
            return 0
        self.grid.pop(low_point_coord)
        return 1 + sum(self.count_basins(p) for p in self.get_neighbours(low_point_coord))
                
    def is_low_point(self, coordinate: complex) -> bool:
        return all(self.grid[coordinate] < self.grid[neighbour] 
                   for neighbour in self.get_neighbours(coordinate))

    def get_neighbours(self, coordinate: complex) -> Generator[complex, None, None]:
        for neighbour in [coordinate + 1, coordinate - 1, coordinate + 1j, coordinate - 1j]:
            if neighbour in self.grid:
                yield neighbour

def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 448
    print(solver.part2())  # 1417248


if __name__ == '__main__':
    main()
