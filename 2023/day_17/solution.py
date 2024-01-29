from heapq import heappop as pop, heappush as push

from utils_anviks.decorators import read_data, stopwatch


@read_data('data.txt', sep2='', _class=int, auto_annotate=True)
@stopwatch
def solution(data: list[list[int]], part: int):
    mapping = {i + j * 1j: data[i][j]
               for i in range(len(data))
               for j in range(len(data[0]))}

    if part == 1:
        return find_best_route(mapping, 1, 3)
    else:
        return find_best_route(mapping, 4, 10)


def find_best_route(mapping: dict[complex, int], min_moves: int, max_moves: int):
    visited = set()
    todo = [(0, 0, 0, 1), (0, 1, 0, 1j)]
    # Unique id for the priority queue so that heapq would never compare the tuple's complex numbers
    uid = 2
    destination = (*mapping,)[-1]

    while todo:
        # accumulated heat loss, unique id, coordinate, direction
        heat_loss, _, coordinate, direction = pop(todo)

        if coordinate == destination:
            return heat_loss

        if (coordinate, direction) in visited:
            continue

        visited.add((coordinate, direction))

        for new_direction in 1j / direction, -1j / direction:
            for steps in range(min_moves, max_moves + 1):
                new_coordinate = coordinate + steps * new_direction

                if new_coordinate not in mapping:
                    break

                uid += 1
                additional_heat_loss = sum(mapping[coordinate + i * new_direction] for i in range(1, steps + 1))

                push(todo, (additional_heat_loss + heat_loss, uid, new_coordinate, new_direction))


if __name__ == '__main__':
    print(solution(1))  # 1065
    print(solution(2))  # 1249
