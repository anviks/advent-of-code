from collections import defaultdict
from functools import reduce

from utils_anviks import read_file, stopwatch


def hash_it(string: str) -> int:
    """
    Hash a string according to the following rules:
        1. Determine the ASCII code for the current character of the string.
        2. Increase the current value by the ASCII code you just determined.
        3. Set the current value to itself multiplied by 17.
        4. Set the current value to the remainder of dividing itself by 256.
    """
    return reduce(lambda acc, char: (acc + ord(char)) * 17, string, 0) % 256


@read_file("data.txt", sep=",")
@stopwatch
def solution(data: list[str], part: int):
    if part == 1:
        return sum(map(hash_it, data))

    boxes = defaultdict(list)

    for step in data:
        if '=' in step:
            lens_label, focal_length = step.split('=')
            focal_length = int(focal_length)
        elif '-' in step:
            lens_label, focal_length = step.split('-')
        else:
            raise ValueError("What?")

        box = hash_it(lens_label)
        lenses = boxes[box]

        if focal_length != '':
            # If a lens with the same label already exists, replace it (maintain the order)
            for i, lens in enumerate(lenses):
                if lens_label == lens[0]:
                    lenses[i] = (lens_label, focal_length)
                    break
            else:
                lenses.append((lens_label, focal_length))
        else:
            # Find and remove the lens with the matching label
            for i, lens in enumerate(lenses):
                if lens_label == lens[0]:
                    lenses.pop(i)
                    break


    total_focusing_power = 0

    # Calculate the total focusing power
    for box, lenses in boxes.items():
        for i, lens in enumerate(lenses, 1):
            total_focusing_power += (1 + box) * i * lens[1]

    return total_focusing_power


if __name__ == '__main__':
    print(solution(1))  # 514639
    print(solution(2))  # 279470
