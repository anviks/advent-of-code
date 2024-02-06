from collections import deque

import networkx as nx
from utils_anviks import read_data, stopwatch

from coordinates import Coordinate3D


class Brick:
    def __init__(self, start: Coordinate3D, end: Coordinate3D):
        self.start = start
        self.end = end

    def __contains__(self, item):
        if not isinstance(item, Coordinate3D):
            return False

        return (self.start.x <= item.x <= self.end.x
                and self.start.y <= item.y <= self.end.y
                and self.start.z <= item.z <= self.end.z)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def __iter__(self):
        """Return all coordinates in the brick"""
        for x in range(self.start.x, self.end.x + 1):
            for y in range(self.start.y, self.end.y + 1):
                for z in range(self.start.z, self.end.z + 1):
                    yield Coordinate3D(x, y, z)

    def __repr__(self):
        return f"{self.__class__.__name__}(start={self.start}, end={self.end})"


def __str_to_coord(string):
    return Coordinate3D(list(map(int, string.split(','))))


@read_data('data.txt', sep2='~', auto_annotate=True)
@stopwatch
def solution(data: list[list[str]], part: int):
    bricks = []

    for start, end in data:
        brick = Brick(__str_to_coord(start), __str_to_coord(end))
        bricks.append(brick)

    graph = nx.DiGraph()

    # Sort by height, assuming start z is always lower than end z
    bricks.sort(key=lambda b: b.start.z)

    highest_points = {}

    # Add brick's id to graph and dictionary, not brick itself, because brick's height
    # will be modified and bricks will be duplicated as a result
    for uid, brick in enumerate(bricks):
        stop = 0

        bricks_below = set()

        for coord in tuple(brick):
            area, _ = coord.extract_axis()
            supporting_brick = highest_points.get(area, (None, 0))

            stop = max(stop, supporting_brick[1])
            bricks_below.add(supporting_brick)

        for br in bricks_below:
            if br[0] is not None and br[1] == stop:
                graph.add_edge(br[0], uid)

        fall = brick.start.z - (stop + 1)
        brick.start.z -= fall
        brick.end.z -= fall

        for coord in tuple(brick):
            area, height = coord.extract_axis()
            highest_points[area] = uid, height

    irremovable = set()

    for vertex in graph.nodes:
        predecessors = tuple(graph.predecessors(vertex))
        if len(predecessors) == 1:
            irremovable.add(predecessors[0])

    if part == 1:
        return len(bricks) - len(irremovable)

    fall_sum = 0

    for src_vertex in irremovable:
        removed = {src_vertex}
        falling_bricks = deque(list(graph.successors(src_vertex)))

        while falling_bricks:
            vertex = falling_bricks.popleft()
            predecessors = list(graph.predecessors(vertex))

            if all(pred in removed for pred in predecessors):
                removed.add(vertex)
                falling_bricks.extend(graph.successors(vertex))

        # Source vertex must not be counted
        fall_sum += len(removed) - 1

    return fall_sum


if __name__ == '__main__':
    print(solution(1))  # 463
    print(solution(2))  # 89727
