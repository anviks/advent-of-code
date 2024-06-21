from utils_anviks import parse_file_content, stopwatch


class AdventOfCodeSolver:
    BRACKET_PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    def __init__(self, input_file_name: str):
        self.data = parse_file_content(input_file_name, ('\n', ''), str)
    
    @stopwatch    
    def part1(self) -> int:
        syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        score = 0
        
        for line in self.data:
            stack = []
            for char in line:
                if char in self.BRACKET_PAIRS:
                    stack.append(char)
                else:
                    if char != self.BRACKET_PAIRS[stack.pop(-1)]:
                        score += syntax_error_scores[char]
                        
        return score
    
    @stopwatch
    def part2(self) -> int:
        autocomplete_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
        multiplier = 5
        scores = []

        for line in self.data:
            stack = []
            for char in line:
                if char in self.BRACKET_PAIRS:
                    stack.append(char)
                else:
                    if char != self.BRACKET_PAIRS[stack.pop(-1)]:
                        break
            else:
                score = 0
                for char in stack[::-1]:
                    score = score * multiplier + autocomplete_scores[char]
                scores.append(score)
        
        return sorted(scores)[len(scores) // 2]


def main() -> None:
    solver = AdventOfCodeSolver('data.txt')
    print(solver.part1())  # 319329
    print(solver.part2())  # 3515583998


if __name__ == '__main__':
    main()
