"""AOC day 2."""


def solution(filename: str, part: int):
    """AOC day 2 solution."""
    with open(filename, encoding="utf-8") as file:
        content = file.read().split("\n")

    if part == 1:
        horizontal = 0
        depth = 0

        for row in content:
            movement, amount = row.split(" ")

            if movement == "up":
                depth -= int(amount)
            elif movement == "down":
                depth += int(amount)
            else:
                horizontal += int(amount)

    else:
        horizontal = 0
        depth = 0
        aim = 0

        for row in content:
            movement, amount = row.split(" ")

            if movement == "up":
                aim -= int(amount)
            elif movement == "down":
                aim += int(amount)
            else:
                horizontal += int(amount)
                depth += aim * int(amount)

    return horizontal * depth


if __name__ == '__main__':
    print(solution("data.txt", 1))
    print(solution("data.txt", 2))
