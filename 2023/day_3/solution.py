from utils_anviks.decorators import read_data, stopwatch


def find_start(matrix: list[list[str]], i: int, j: int) -> tuple[int, int]:
    """Find the starting point of the number in the matrix."""
    assert matrix[i][j].isdigit()

    while matrix[i][j - 1].isdigit():
        j -= 1

    return i, j


def get_surrounding_number_coords(matrix: list[list[str]], i: int, j: int) -> set:
    """Get starting coordinates of surrounding numbers."""
    part_number_coords = set()

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue

            surrounding_element = matrix[i + x][j + y]
            if surrounding_element.isdigit():
                part_number_coords.add(find_start(matrix, i + x, j + y))

    return part_number_coords


@stopwatch
@read_data(sep2="")
def solution(data: list[list[str]], part: int):
    total = 0

    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            element = data[i][j]
            part1_predicate = part == 1 and not element.isalnum() and element != '.'
            part2_predicate = part == 2 and element == '*'

            if not part1_predicate and not part2_predicate:
                continue

            part_number_coords = get_surrounding_number_coords(data, i, j)

            if part == 1 or len(part_number_coords) == 2:
                product = 1

                for x, y in part_number_coords:
                    num = ""

                    while (x < len(data)
                           and y < len(data[x])
                           and data[x][y].isdigit()):
                        num += data[x][y]
                        y += 1

                    if part == 1:
                        total += int(num)
                    else:
                        product *= int(num)

                if part == 2:
                    total += product

    return total


if __name__ == '__main__':
    print(solution(1))  # 560670
    print(solution(2))  # 91622824
