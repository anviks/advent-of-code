import re
from functools import cache
from itertools import product

from utils_anviks import read_file, stopwatch


@read_file("sample.txt", sep2=" ")
@stopwatch
def solution(data: list[list[str]], part: int):
    for i, row in enumerate(data):
        data[i][1] = tuple(map(int, row[1].split(',')))
        if part == 2:
            data[i][0] = '?'.join([data[i][0]] * 5) + ' '
            data[i][1] = data[i][1] * 5
        else:
            data[i][0] += ' '

    return sum(count_permutations_2(strings, counts) for strings, counts in data)


def is_valid_permutation(springs: tuple[str], counts: tuple[int]) -> bool:
    """Takes 30s for part 1"""
    row_s = ''.join(springs)
    matches = re.findall(r'#+', row_s)
    lengths = tuple(len(s) for s in matches)

    return lengths == counts


def is_valid_permutation_2(springs: tuple[str], counts: tuple[int]) -> bool:
    expected_length = len(counts)
    prev_spr_damaged = False
    comb_counts = []
    last_cc_index = -1

    for spr in springs:
        if spr == '#':
            if prev_spr_damaged:
                comb_counts[-1] += 1

                # Saves another 0.1 seconds
                if comb_counts[last_cc_index] > counts[last_cc_index]:
                    return False
            else:
                comb_counts.append(1)
                last_cc_index += 1
                prev_spr_damaged = True

                # Means that comb_counts exceeded expected length by 1.
                if last_cc_index == expected_length:
                    return False
        else:
            prev_spr_damaged = False

            # Early exit if the combination is invalid, halving the time taken for part 1 (10s -> 5.5s)
            if last_cc_index != -1 and comb_counts[last_cc_index] != counts[last_cc_index]:
                return False

    return tuple(comb_counts) == counts


def count_permutations(counts, springs):
    arrangements = 0
    possibilities = []
    for spr in springs:
        if spr == '?':
            possibilities.append(['#', '.'])
        else:
            possibilities.append([spr])
    for comb in product(*possibilities):
        if is_valid_permutation_2(comb, counts):
            arrangements += 1
    return arrangements


@cache
def count_permutations_2(springs, counts, broken_spring_streak=0):
    if not springs:
        return not counts and not broken_spring_streak
    results = 0
    possibilities = ['.', '#'] if springs[0] == '?' else springs[0]
    for p in possibilities:
        if p == '#':
            results += count_permutations_2(springs[1:], counts, broken_spring_streak + 1)
        else:
            if broken_spring_streak > 0:
                if counts and counts[0] == broken_spring_streak:
                    results += count_permutations_2(springs[1:], counts[1:])
            else:
                results += count_permutations_2(springs[1:], counts)
    return results


if __name__ == '__main__':
    print(solution(1))  # 7599
    print(solution(2))  # 15454556629917
