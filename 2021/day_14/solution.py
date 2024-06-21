from collections import Counter

from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    def __init__(self, input_file_name: str):
        polymer, _, *data = parse_file_content(input_file_name, ('\n',), str)
        self.pairs = Counter(zip(polymer, polymer[1:]))
        self.chars = Counter(polymer)
        
        self.map = {}
        for row in data:
            k, v = row.split(' -> ')
            self.map[tuple(k)] = v
            
    def insert_elements(self, count: int):
        for _ in range(count):
            for (first, second), count in self.pairs.copy().items():
                new_char = self.map[first, second]
                
                self.pairs[first, second] -= count
                self.pairs[first, new_char] += count
                self.pairs[new_char, second] += count

                self.chars[new_char] += count
    
    @stopwatch
    def part1(self) -> int:
        self.insert_elements(10)
        elements = self.chars.most_common()

        return elements[0][1] - elements[-1][1]
        
    
    @stopwatch
    def part2(self) -> int:
        self.insert_elements(40)
        elements = self.chars.most_common()

        return elements[0][1] - elements[-1][1]


def main() -> None:
    print(AdventOfCodeSolver('data.txt').part1())  # 4517
    print(AdventOfCodeSolver('data.txt').part2())  # 4704817645083


if __name__ == '__main__':
    main()