from dataclasses import dataclass, field
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
import numpy as np

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ('\n', ''), str)

def surrounding_rolls(row: int, col: int) -> int:
    rolls = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            r, c = row + i, col + j
            if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == '@':
                rolls += 1
    return rolls


def get_surrounding_rolls(row: int, col: int) -> list[tuple[int, int]]:
    rolls = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            r, c = row + i, col + j
            if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == '@':
                rolls.append((r, c))
    return rolls

@stopwatch
def part1():
    accessible = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            accessible += data[i][j] == '@' and surrounding_rolls(i, j) < 4
    
    return accessible


@dataclass(unsafe_hash=True)
class Node:
    row: int
    column: int
    neighbours: set['Node'] = field(default_factory=set, init=False, repr=False, hash=False, compare=False)

    def add_neighbour(self, other: 'Node') -> None:
        self.neighbours.add(other)

    def remove_neighbour(self, other: 'Node') -> None:
        self.neighbours.discard(other)


def prune_graph(nodes: list[Node]):
    to_remove = [node for node in nodes if len(node.neighbours) <= 3]
    x = 0

    while to_remove:
        if x in [0, 13, 25, 32,   36,    37, 39, 40, 41, 42, 43]:
            for i in range(10):
                for j in range(10):
                    if Node(i, j) in nodes:
                        print('@', end='')
                    else:
                        print('.', end='')
                print()
            print()

        node = to_remove.pop(0)
        if node in nodes:
            nodes.remove(node)
            x += 1
        for neighbour in list(node.neighbours):
            neighbour.remove_neighbour(node)
            if len(neighbour.neighbours) <= 3 and neighbour in nodes:
                to_remove.append(neighbour)


@stopwatch
def part2():
    # ATTEMPT 1

    # accessible = 0
    # temp_accessible = -1

    # while temp_accessible != 0:
    #     temp_accessible = 0

    #     for i in range(len(data)):
    #         for j in range(len(data[i])):
    #             temp_accessible += data[i][j] == '@' and surrounding_rolls(i, j) < 4

    #     accessible += temp_accessible

    rolls = set()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@':
                rolls.add((i, j))
    
    removed = 0
    temp = -1

    while temp != 0:
        temp = 0

        for roll in rolls.copy():
            nbs = 0
            for nb in get_surrounding_rolls(*roll):
                if nb in rolls:
                    nbs += 1
            if nbs <= 3:
                rolls.remove(roll)
                temp += 1

        removed += temp
    
    return removed
        

    # ATTEMPT 2

    # nodes: dict[tuple[int, int], Node] = {}

    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         if data[i][j] == '@':
    #             nodes[i, j] = Node(i, j)
    #             for roll in get_surrounding_rolls(i, j):
    #                 nodes[i, j].add_neighbour(nodes.get(roll, Node(*roll)))
    
    # node_list = list(nodes.values())
    # before = len(node_list)
    # prune_graph(node_list)
    # after = len(node_list)

    # return before - after


if __name__ == "__main__":
    print(part1())  # 1491
    print(part2())






import weakref

class Item:
    def __init__(self, name):
        self.name = name
        self.refs = []  # list[weakref.ref to Item]

    def add_ref(self, other):
        self.refs.append(weakref.ref(other))

    def get_living_refs(self):
        return [ref() for ref in self.refs if ref() is not None]


a = Item("a")
b = Item("b")
c = Item("c")

a.add_ref(b)
b.add_ref(c)

items = [a, b, c]

items.remove(b)  # b is no longer strongly referenced → GC removes it

print(a.get_living_refs())   # b disappears automatically

