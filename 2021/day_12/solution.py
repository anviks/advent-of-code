from collections import defaultdict

from utils_anviks import parse_file_content, stopwatch
import networkx as nx


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        self.data = parse_file_content(input_file_name, sep2='-')
        self.graph = nx.Graph()
        for row in self.data:
            self.graph.add_edge(*row)
    
    @stopwatch
    def part1(self) -> int:
        return self.find_paths(1)
    
    @stopwatch
    def part2(self) -> int:
        return self.find_paths(2)

    def find_paths(self, part: int, cave: str = 'start', visited_lowercase: set | None = None):
        if visited_lowercase is None:
            visited_lowercase = set()
    
        if cave == 'end':
            return 1
        
        if cave in visited_lowercase:
            if cave == 'start':
                return 0
            if part == 1:
                return 0
            else:
                part = 1

        n = 0

        for neighbour in self.graph.neighbors(cave):
            n += self.find_paths(part, neighbour, (visited_lowercase | {cave}) if cave.islower() else visited_lowercase)
                    
        return n


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 5076
    print(solver.part2())  # 145643  0.5 seconds


if __name__ == '__main__':
    main()
