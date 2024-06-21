import re

from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n',), str)
    
    # Part 1: Sum of game IDs, where limits are not exceeded
    # Part 2: Sum of products of minimum possible amount of cubes
    total = 0

    limit_red = 12
    limit_green = 13
    limit_blue = 14

    for line in data:
        game_id = int(re.search(r"((?<=Game )\d+(?=:))", line).group())
        red_counts = [int(count) for count in re.findall(r"\d+(?= red)", line)]
        green_counts = [int(count) for count in re.findall(r"\d+(?= green)", line)]
        blue_counts = [int(count) for count in re.findall(r"\d+(?= blue)", line)]

        if part == 1:
            if all((all(count <= limit_red for count in red_counts),
                    all(count <= limit_green for count in green_counts),
                    all(count <= limit_blue for count in blue_counts))):
                total += game_id
        else:
            total += max(red_counts) * max(green_counts) * max(blue_counts)

    return total


if __name__ == '__main__':
    print(solution(1))  # 2237
    print(solution(2))  # 66681
