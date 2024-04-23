from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        self.data = parse_file_content(input_file_name, sep2='', _class=int)
        self.grid = None
        
    def initialize_grid(self):
        self.grid = {complex(i, j): square
                     for i, row in enumerate(self.data)
                     for j, square in enumerate(row)}
    
    @stopwatch    
    def part1(self) -> int:
        self.initialize_grid()
        return sum(self.simulate_step() for _ in range(100))
    
    @stopwatch
    def part2(self) -> int:
        self.initialize_grid()
        steps_taken = 0
        
        while set(self.grid.values()) != {0}:
            self.simulate_step()
            steps_taken += 1
            
        return steps_taken
    
    def simulate_step(self) -> int:
        flashes = 0
        
        for coord in self.grid:
            self.grid[coord] += 1
            
        flashing = {coord for coord in self.grid if self.grid[coord] > 9}
        
        while flashing:
            coord = flashing.pop()
            self.grid[coord] = 0
            flashes += 1
            
            for neighbour in self.get_neighbours(coord):
                self.grid[neighbour] += 1
                if self.grid[neighbour] > 9:
                    flashing.add(neighbour)
        
        return flashes
                
    def get_neighbours(self, coord: complex):
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour = coord + complex(i, j)
                # If the neighbour is not the current cell, and it exists in the grid, and it isn't 0.
                if neighbour != coord and self.grid.get(neighbour):
                    yield neighbour


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 1591
    print(solver.part2())  # 314


if __name__ == '__main__':
    main()
