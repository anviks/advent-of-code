"""AOC day 2."""
from utils_anviks import parse_file_content


def solution(part: int):
    """AOC day 2 solution."""
    content = parse_file_content('data.txt', ('\n', ' '), str)

    horizontal = 0
    depth = 0
    aim = 0

    for row in content:
        movement, amount = row
        amount = int(amount)

        if part == 1:
            if movement == "up":
                depth -= amount
            elif movement == "down":
                depth += amount
            else:
                horizontal += amount
        else:
            if movement == "up":
                aim -= amount
            elif movement == "down":
                aim += amount
            else:
                horizontal += amount
                depth += aim * amount

    return horizontal * depth


if __name__ == '__main__':
    print(solution(1))  # 1728414
    print(solution(2))  # 1765720035
