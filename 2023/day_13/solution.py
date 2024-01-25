from utils_anviks.decorators import read_data, stopwatch


@read_data("data.txt", sep="\n\n", sep2="\n")
@stopwatch
def solution(data: list[list[str]], part: int):
    is_part_one = part == 1
    acc = 0

    for mirror in data:
        row_index = find_reflection_index(mirror, is_part_one)
        transposed_mirror = list(map(list, zip(*mirror)))
        column_index = find_reflection_index(transposed_mirror, is_part_one)

        acc += column_index
        acc += 100 * row_index

    return acc


def find_reflection_index(mirror: list[str | list[str]], is_part_one: bool) -> int:
    """
    Find the index of the row where the mirror image is reflected.

    The mirror is considered to be reflected if the reversed upper part of the mirror image is equal to the lower part.
    The length of the parts can be anything, but they must be equal in size and one of them must touch
    the top or the bottom edge of the mirror, meaning that if the mirror is 10x8, it will be considered
    reflected even if the parts are 1x8 in size, provided that they are the first or last two rows of the mirror.

    :param mirror: The mirror image matrix.
    :param is_part_one: Whether to find the index for part one or part two of advent of code.
    :return: The index of where the bottom part of the mirror image starts.
    """
    for i in range(1, len(mirror)):
        if is_part_one and mirror[i] != mirror[i - 1]:
            continue

        # No need to make them equal in length here, because the zip will handle it in the are_equal function
        upper_part = mirror[i - 1::-1]
        lower_part = mirror[i:]

        if are_equal(upper_part, lower_part, not is_part_one):
            return i

    return 0


def are_equal(upper: list[str | list[str]], lower: list[str | list[str]], required_discrepancies: int) -> bool:
    """
    Check if two matrices are (almost) equal.

    :param upper: upper part of the matrix
    :param lower: lower part of the matrix
    :param required_discrepancies: the number of discrepancies required for the matrices to be considered equal
    :return: whether the matrices are equal
    """
    discrepancies = 0

    for upper_row, lower_row in zip(upper, lower):
        for upper_elem, lower_elem in zip(upper_row, lower_row):
            if upper_elem != lower_elem:
                discrepancies += 1
                if discrepancies > required_discrepancies:
                    return False

    return discrepancies == required_discrepancies


if __name__ == '__main__':
    print(solution(1))  # 34993
    print(solution(2))  # 29341
