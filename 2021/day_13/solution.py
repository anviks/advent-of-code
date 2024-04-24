import itertools
import cProfile

from memory_profiler import profile
from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    @stopwatch
    def __init__(self, input_file_name: str):
        data = parse_file_content(input_file_name, sep='\n\n', sep2='\n')
        coords = set()
        for coord in data[0]:
            coords.add(tuple(map(int, coord.split(','))))
        self.grid = [
            [(i, j) in coords for i in range(max(coords)[0] + 1)]
            for j in range(max(coords, key=lambda c: c[1])[1] + 1)
        ]
        self.folds = []
        for fold in data[1]:
            axis, coord = fold.split(' ')[-1].split('=')
            self.folds.append((axis, int(coord)))

    @stopwatch
    def part1(self) -> int:
        self.fold(1)
        chain = itertools.chain(*self.grid)
        
        return sum(chain)

    @stopwatch
    def part2(self) -> str:
        self.fold()  # Finish folding

        result = ''
        for i, line in enumerate(self.grid):
            for j, flag in enumerate(line):
                result += '#' if flag else ' ' 
            result += '\n'

        return result
    
    def fold(self, times: int | None = None):
        iteration = 0
        
        for axis, coord in self.folds:            
            if axis == 'x':
                self.grid = list(map(list, zip(*self.grid)))
        
            bottom_half = self.grid[coord + 1:]
            self.grid = self.grid[:coord]
            assert len(bottom_half) == len(self.grid)
        
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    self.grid[i][j] |= bottom_half[-i - 1][j]
        
            if axis == 'x':
                self.grid = list(map(list, zip(*self.grid)))

            iteration += 1
            if iteration == times:
                break
        
        self.folds = self.folds[times:]


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 745
    print(solver.part2())  # ABKJFBGC


if __name__ == '__main__':
    main()
