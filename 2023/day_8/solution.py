import math
import re
import time

from utils_anviks.decorators import read_data, stopwatch


@read_data
@stopwatch
def solution(data: list[str], part: int):
    # 0 - left, 1 - right
    instructions = [0 if letter == 'L' else 1 for letter in data[0]]
    # {'AAA': ('BBB', 'CCC'), 'BBB': ('AAA', 'CCC'), ...}
    movement_map = {}

    for line in data[2:]:
        matches = re.search(r"(\w{3}) = \((\w{3}), (\w{3})\)", line).groups()
        movement_map[matches[0]] = (matches[1:])

    if part == 1:
        return solve_part_one(instructions, movement_map)
    else:
        return solve_part_two(instructions, movement_map)



def solve_part_one(instructions, movement_map):
    steps = 0
    instr_index = 0

    current_location = "AAA"
    target = "ZZZ"

    while current_location != target:
        instruction = instructions[instr_index]
        current_location = movement_map[current_location][instruction]

        steps += 1
        instr_index += 1
        instr_index %= len(instructions)

    return steps


def solve_part_two(instructions, movement_map):
    current_locations = []

    for location in movement_map:
        if location[-1] == 'A':
            # ['AAA', 0] - location, steps
            current_locations.append([location, 0])

    for i in range(len(current_locations)):
        curr_loc = current_locations[i]
        instr_index = 0

        while curr_loc[0][-1] != 'Z':
            instruction = instructions[instr_index]
            target = movement_map[curr_loc[0]]

            curr_loc[0] = target[instruction]
            curr_loc[1] += 1
            instr_index += 1
            instr_index %= len(instructions)

    return math.lcm(*[loc[1] for loc in current_locations])


if __name__ == '__main__':
    print(solution(1))  # 20569
    print(solution(2))  # 21366921060721
