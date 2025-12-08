from itertools import combinations
from math import sqrt, prod
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = [tuple(line) for line in parse_file_content(file_path, ("\n", ","), int)]

box_pairs = list(combinations(data, 2))
box_pairs.sort(
    key=lambda boxes: sqrt(sum((boxes[1][i] - boxes[0][i]) ** 2 for i in range(3)))
)


@stopwatch
def part1():
    circuits: list[set[tuple[int, ...]]] = []
    counter = 0

    for box1, box2 in box_pairs:
        box1_circ = box2_circ = None
        for circ in circuits:
            if box1 in circ:
                box1_circ = circ
            elif box2 in circ:
                box2_circ = circ

        match box1_circ, box2_circ:
            case None, None:
                circuits.append({box1, box2})
            case _, None:
                box1_circ.add(box2)
            case None, _:
                box2_circ.add(box1)
            case _, _:
                box1_circ.update(box2_circ)
                circuits.remove(box2_circ)

        counter += 1
        if counter == 1000:
            break

    return prod(sorted(map(len, circuits), reverse=True)[:3])


@stopwatch
def part2():
    circuits: list[set[tuple[int, ...]]] = []
    result = 0

    for box1, box2 in box_pairs:
        box1_circ = box2_circ = None
        for circ in circuits:
            if box1 in circ:
                box1_circ = circ
            elif box2 in circ:
                box2_circ = circ

        match box1_circ, box2_circ:
            case None, None:
                circuits.append({box1, box2})
            case _, None:
                box1_circ.add(box2)
                result = box1[0] * box2[0]
            case None, _:
                box2_circ.add(box1)
                result = box1[0] * box2[0]
            case _, _:
                result = box1[0] * box2[0]
                box1_circ.update(box2_circ)
                circuits.remove(box2_circ)

        if len(circuits) == 1 and len(circuits[0]) == len(data):
            break

    return result


if __name__ == "__main__":
    print(part1())  # 181584        | 0.011 seconds
    print(part2())  # 8465902405    | 0.018 seconds
