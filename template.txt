from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        self.data = parse_file_content(input_file_name)
    
    @stopwatch    
    def part1(self) -> int:
        pass
    
    @stopwatch
    def part2(self) -> int:
        pass


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())
    print(solver.part2())


if __name__ == '__main__':
    main()
