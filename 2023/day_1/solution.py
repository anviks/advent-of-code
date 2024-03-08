import re

from utils_anviks import read_file, stopwatch


@stopwatch
@read_file('data.txt')
def solution(data: list[str], part: int):
    total = 0
    num_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in data:
        first_num = last_num = None

        for i in range(len(line)):
            char = line[i]
            if char.isdigit():
                first_num = first_num or char  # no zeroes
                last_num = char
            elif part == 2:
                for k in num_map:
                    if line[i:i + len(k)] == k:
                        first_num = first_num or num_map[k]  # no zeroes
                        last_num = num_map[k]

        total += int(first_num + last_num)

    return total


@read_file('data.txt')
@stopwatch
def solution_horrible(data: list[str], part: int):
    if part == 1:
        pass
    else:
        return sum([int((wtd := {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                                 "eight": "8", "nine": "9"}).get(
            (res := re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line))[0], res[0]) + wtd.get(
            res[-1], res[-1])) for line in data])


if __name__ == '__main__':
    print(solution(1))  # 55477
    print(solution(2))  # 54431

    print(solution_horrible(2))
