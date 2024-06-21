from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution():
    data = parse_file_content('data.txt', ('\n', ' '), int)
    next_values = []
    prev_values = []

    for history in data:
        differences = [history]

        # Calculate the differences between the numbers in the history and differences between the differences.
        while any(differences[-1]):
            last_diff = differences[-1]
            differences.append([])
            for i in range(1, len(last_diff)):
                differences[-1].append(last_diff[i] - last_diff[i - 1])

        next_val = 0
        prev_val = 0
        differences[-1].append(next_val)
        differences[-1].insert(0, prev_val)

        # Iterate backwards through the differences and calculate the next and previous values.
        for i in range(1, len(differences)):
            next_val = differences[-i - 1][-1] + differences[-i][-1]
            prev_val = differences[-i - 1][0] - differences[-i][0]
            differences[-i - 1].append(next_val)
            differences[-i - 1].insert(0, prev_val)

        next_values.append(next_val)
        prev_values.append(prev_val)

    return sum(next_values), sum(prev_values)


if __name__ == '__main__':
    solution = solution()
    print(solution[0])  # 1725987467
    print(solution[1])  # 971
