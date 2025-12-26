from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch, parse_string

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
*_, regs = parse_file_content(file_path, ("\n\n",), str)
regions = parse_string(regs, ("\n", re.compile(r"\D+")), int)


@stopwatch
def part1():
    """
    Idea taken from https://www.reddit.com/r/adventofcode/comments/1pkje0o/comment/ntlkg9i
    I can't believe this works...
    """
    return sum(w // 3 * h // 3 >= sum(n) for w, h, *n in regions)


if __name__ == "__main__":
    print(part1())  # 546   | 0.00027 seconds
