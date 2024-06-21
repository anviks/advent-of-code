from itertools import combinations, accumulate

from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n', ''), str)
    expansion_multiplier = 2 if part == 1 else 1_000_000
    length_sum = 0

    galaxies = {(i, j)
                for i in range(len(data))
                for j in range(len(data[i]))
                if data[i][j] == "#"}

    # dimension is a tuple of either row or column indices.
    for dimension in zip(*galaxies):
        # dimension_widths is a list of the widths of the rows or columns
        # if there are no galaxies in the row or column, the width is 1 * expansion_multiplier due to the expansion
        dimension_widths = []
        for n in range(max(dimension) + 1):
            if n in set(dimension):
                dimension_widths.append(1)
            else:
                dimension_widths.append(expansion_multiplier)

        # distances_from_start is a list of the cumulative sums of the widths of the rows or columns
        distances_from_start = list(accumulate(dimension_widths))

        # For each pair of galaxies, add the distance between them (one dimension) to the length_sum.
        for start, end in combinations(dimension, 2):
            length_sum += abs(distances_from_start[start] - distances_from_start[end])

    return length_sum


if __name__ == '__main__':
    print(solution(1))  # 9724940
    print(solution(2))  # 569052586852
