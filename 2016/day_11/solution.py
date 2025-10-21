from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch
from copy import deepcopy
from heapq import heappop, heappush, heapify
from itertools import combinations

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", re.compile(r"(?: and)?,? a "), " "), str)

for floor in data:
    for item in floor[1:]:
        # Remove "-compatible" suffixes and possible trailing punctuations
        if item[1].startswith("generator"):
            item[1] = "generator"
        else:
            item[1] = "microchip"
            item[0] = item[0].split("-")[0]


def get_items_as_numbers(stuff: list[list[list[str]]]):
    items: list[list[int]] = []
    item_map: dict[str, int] = {}
    current = 1

    for floor in stuff:
        items.append([])

        for item in floor[1:]:
            if item[0] not in item_map:
                item_map[item[0]] = current
                current += 1

            mul = 1
            if item[1] == "microchip":
                mul = -1

            items[-1].append(mul * item_map[item[0]])

    return tuple(map(lambda ls: tuple(sorted(ls)), items))


def is_valid_floor(floor: tuple[int, ...]):
    # valid if no generators
    if all(item < 0 for item in floor):
        return True

    for item in floor:
        # invalid if microchip doesn't have a corresponding generator
        if item < 0 and -item not in floor:
            return False

    return True


def solve(input_data: list[list[list[str]]]):
    items_tuple = get_items_as_numbers(input_data)
    initial = (0, items_tuple)
    queue = [(0, 0, initial)]
    heapify(queue)
    seen = set()

    while queue:
        _, cost, state = heappop(queue)
        elevator, floors = state

        if elevator == 3 and all(len(floor) == 0 for floor in floors[:-1]):
            return cost

        directions = [d for d in (-1, 1) if 0 <= elevator + d < 4]
        take_with = tuple(combinations(floors[elevator], 2)) + tuple(
            combinations(floors[elevator], 1)
        )

        for direction in directions:
            # Optimization
            if direction == -1 and len(floors[elevator - 1]) == 0:
                continue

            for items in take_with:
                new_floors = list(floors)
                new_floors[elevator] = tuple(
                    x for x in floors[elevator] if x not in items
                )
                new_floors[elevator + direction] = tuple(
                    sorted(floors[elevator + direction] + items)
                )

                new_floors_tuple = tuple(new_floors)

                if (elevator + direction, new_floors_tuple) in seen:
                    continue

                # validate new state
                if not is_valid_floor(new_floors[elevator]) or not is_valid_floor(
                    new_floors[elevator + direction]
                ):
                    continue

                seen.add((elevator + direction, new_floors_tuple))
                # prioritise states with more progress
                priority = cost - len(new_floors[3]) * 5
                heappush(
                    queue,
                    (priority, cost + 1, (elevator + direction, new_floors_tuple)),
                )


@stopwatch
def part1():
    return solve(data)


@stopwatch
def part2():
    new_data = deepcopy(data)
    new_data[0].extend(
        [
            ["elerium", "generator"],
            ["elerium", "microchip"],
            ["dilithium", "generator"],
            ["dilithium", "microchip"],
        ]
    )

    return solve(new_data)


if __name__ == "__main__":
    print(part1())  # 33    | 0.042 seconds
    print(part2())  # 57    | 18.62 seconds
