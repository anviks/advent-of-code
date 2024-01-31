from utils_anviks import read_data, stopwatch


@read_data(filename='data.txt', sep2=' ', auto_annotate=True)
@stopwatch
def solution_part_one(data: list[list[str]]):
    current_location = 0
    holes = {}

    directions_map = {
        'U': -1,
        'D': 1,
        'L': -1j,
        'R': 1j
    }

    min_imag = max_imag = min_real = max_real = 0

    for direction, distance, colour in data:
        distance = int(distance)

        if direction in "UD":
            my_range = 0, distance + 1
        else:
            my_range = 1, distance

        for step in range(*my_range):
            holes[current_location + directions_map[direction] * step] = directions_map[direction]

        current_location += directions_map[direction] * distance

        min_real = min(min_real, current_location.real)
        max_real = max(max_real, current_location.real)
        min_imag = min(min_imag, current_location.imag)
        max_imag = max(max_imag, current_location.imag)

    lagoon_area = 0
    direction_cache = None

    for i in range(int(min_real), int(max_real + 1)):
        in_perimeter = False
        for j in range(int(min_imag), int(max_imag) + 1):
            location = i + j * 1j
            direction = holes.get(location)
            if direction is not None:
                if direction.imag == 0:
                    if location + direction in holes and location - direction in holes:  # consider removing 2nd part of the condition
                        in_perimeter = not in_perimeter
                    elif direction_cache is not None:
                        if direction == direction_cache:
                            in_perimeter = not in_perimeter
                    else:
                        direction_cache = direction

                lagoon_area += 1
            else:
                direction_cache = None

                if in_perimeter:
                    lagoon_area += 1

    return lagoon_area


if __name__ == '__main__':
    print(solution_part_one())
