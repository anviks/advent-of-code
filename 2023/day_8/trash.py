import time


def solve_part_two(instructions, movement_map):
    steps = 0
    instr_index = 0

    current_locations = []

    for location in movement_map:
        if location[-1] == 'A':
            current_locations.append(location)

    my_timer = time.perf_counter()

    # With this solution, reaching 21_366_921_060_721 iterations is required, however,
    # with 1_000_000 iterations per second, it would take 247.3 days. Wrote this bad implementation
    # for fun
    while not check(current_locations):
        instruction = instructions[instr_index]
        for i in range(len(current_locations)):
            if instruction == 'L':
                current_locations[i] = movement_map[current_locations[i]][0]
            elif instruction == 'R':
                current_locations[i] = movement_map[current_locations[i]][1]

        steps += 1
        instr_index += 1
        instr_index %= len(instructions)

        if time.perf_counter() - my_timer >= 1:
            my_timer = time.perf_counter()
            print(steps)

    return steps


def check(locations: list):
    for loc in locations:
        if loc[-1] != 'Z':
            return False

    return True
