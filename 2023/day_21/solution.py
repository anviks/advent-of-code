import time

from utils_anviks import read_data, stopwatch


@read_data('data.txt', sep2='', auto_annotate=True)
@stopwatch
def solution(data: list[list[str]], part: int):
    garden = {}
    possible_tiles = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            plot = data[i][j]

            if plot == 'S':
                plot = '.'
                possible_tiles.add(i + j * 1j)

            garden[i + j * 1j] = plot

    for i in range(500):
        if i % 131 == 65:
            print(len(possible_tiles), end=', ')

        temp_set = set()

        for tile in possible_tiles:
            for offset in (1, -1, 1j, -1j):
                next_tile = tile + offset
                if garden.get(next_tile.real % 131 + next_tile.imag % 131 * 1j) == '.':
                    temp_set.add(next_tile)

        temp_set.discard(None)
        possible_tiles = temp_set

    return len(possible_tiles)


def extend_sequence(sequence, length: int):
    differences = [sequence]

    # Calculate the differences between the numbers in the history and differences between the differences.
    while any(differences[-1]):
        last_diff = differences[-1]
        differences.append([])
        for i in range(1, len(last_diff)):
            differences[-1].append(last_diff[i] - last_diff[i - 1])

    next_val = 0
    differences[-1].append(next_val)

    for i in range(1, len(differences)):
        vvv = len(differences[-i - 1]) - 1
        # Iterate backwards through the differences and calculate the next and previous values.
        for _ in range(length):
            if i != 1:
                next_val = differences[-i - 1][-1] + differences[-i][vvv]
            else:
                next_val = differences[-i - 1][-1] + differences[-i][-1]
            differences[-i - 1].append(next_val)
            vvv += 1


if __name__ == '__main__':
    print(solution(1))  # 3841
    # print(solution(2))  # 636391426712747
    z = [3947, 35153, 97459, 190865]
    # [3947, 35153, 97459, 190865, 315371, 470977, 657683]

    extend_sequence(z, 202300 - 3)

    print(z[-1] == 636391426712747)

