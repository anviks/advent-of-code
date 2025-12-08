from itertools import product
from math import sqrt
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
import networkx as nx

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file0
data = [tuple(line) for line in parse_file_content(file_path, ('\n', ','), int)]


@stopwatch
def part1():
    box_pairs = [(x,y) for x in data for y in data if x != y]
    box_pairs.sort(key=lambda boxes: sqrt(sum((boxes[1][i] - boxes[0][i]) ** 2 for i in range(3))))

    circuits: list[set[tuple[int, ...]]] = []

    for box1, box2 in box_pairs:
        for circ in circuits:
            if box1 in circ or box2 in circ:
                circ.add(box1)
                circ.add(box2)
                break
        else:
            circuits.append({box1, box2})
    

@stopwatch
def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
