from collections import deque

from utils_anviks import parse_file_content, stopwatch


def parse_garden(matrix: list[list[str]]):
    garden = {}
    start = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            plot = matrix[i][j]

            if plot == 'S':
                plot = '.'
                start = complex(i, j)

            garden[complex(i, j)] = plot

    return garden, start


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n', ''), str)
    garden, start = parse_garden(data)
    garden_length = len(data)

    # 64 steps are needed for part 1 and 458 steps are needed to get 4 results for establishing the pattern for part 2.
    step_limit = 64 if part == 1 else 458

    visited = {}
    todo = deque([(start, 0)])

    vals = []
    largest_steps = 0

    while todo:
        loc, steps = todo.popleft()

        if steps == step_limit + 1:
            break

        # 65 is the remainder from the division of 26501365 (steps needed for part 2) by the length of the garden.
        if steps > largest_steps and (steps - 1) % garden_length == 65:
            largest_steps = steps
            vals.append(len([v for v in visited.values() if v % 2 == (steps * garden_length + 65) % 2]))

        if loc in visited:
            continue

        visited[loc] = steps

        for offset in (1, -1, 1j, -1j):
            new_loc = loc + offset
            if garden[new_loc.real % garden_length + new_loc.imag % garden_length * 1j] == '.':
                todo.append((new_loc, steps + 1))

    vals.append(len([v for v in visited.values() if v % 2 == 0]))

    if part == 1:
        return vals[0]

    # 26501365 is the number of steps needed for part 2.
    extend_sequence(vals, 26501365 // garden_length - 3)

    return vals[-1]


def extend_sequence(sequence, length: int):
    """Function taken from day 9 solution."""
    differences = [sequence]

    # Calculate differences between the numbers in the sequence and differences between the differences
    # until they are all 0.
    while any(differences[-1]):
        last_diff = differences[-1]
        differences.append([])
        for i in range(1, len(last_diff)):
            differences[-1].append(last_diff[i] - last_diff[i - 1])

    # Start extending each difference sequence by adding the last sequence's last value to the next sequence's last value.
    next_val = 0
    differences[-1].append(next_val)

    # Iterate backwards through the differences and calculate [length] next values.
    for i in range(1, len(differences)):
        diff_index = len(differences[-i - 1]) - 1

        for _ in range(length):
            # No need to extend the second from last sequence as it only has one value.
            if i == 1:
                break

            # Set the index to 0, because all the values in the second from last sequence are the same.
            if i == 2:
                diff_index = 0

            next_val = differences[-i - 1][-1] + differences[-i][diff_index]
            differences[-i - 1].append(next_val)
            diff_index += 1


if __name__ == '__main__':
    print(solution(1))  # 3841
    print(solution(2) == 636391426712747)  # 636391426712747
