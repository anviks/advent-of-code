from utils_anviks import parse_file_content, stopwatch


def part_one_visualisation(data: list[list[str]]):
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
        dir_value = directions_map[direction]

        for step in range(1, distance + 1):
            holes[current_location + dir_value * step] = dir_value

        current_location += dir_value * distance

        min_real = min(min_real, current_location.real)
        max_real = max(max_real, current_location.real)
        min_imag = min(min_imag, current_location.imag)
        max_imag = max(max_imag, current_location.imag)

    lagoon_area = 0
    arr = []
    dir_to_str = {
        -1: '^',
        1: 'v',
        -1j: '<',
        1j: '>'
    }

    for i in range(int(min_real), int(max_real + 1)):
        arr.append([])
        for j in range(int(min_imag), int(max_imag) + 1):
            location = i + j * 1j
            direction = holes.get(location)
            arr[-1].append(dir_to_str.get(direction) or '.')

    with open('visual.txt', 'w') as f:
        f.write('\n'.join(''.join(map(str, row)) for row in arr))

    return lagoon_area


def shoelace_formula(vertices):
    n = len(vertices)
    area = 0

    for i in range(n - 1):
        area += vertices[i].real * vertices[i + 1].imag
        area -= vertices[i].imag * vertices[i + 1].real

    area += vertices[n - 1].real * vertices[0].imag
    area -= vertices[n - 1].imag * vertices[0].real

    area = abs(area) / 2.0
    return area


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n', ' '), str)
    sections = []
    current_position = 0

    directions_map = {
        'U': -1,
        'D': 1,
        'L': -1j,
        'R': 1j
    }

    if part == 1:
        part_one_visualisation(data)

    for direction, steps, colour in data:
        if part == 1:
            direction = directions_map[direction]
            steps = int(steps)
        else:
            steps, direction = int(colour[2:-2], 16), 1j / 1j ** int(colour[-2])

        start = current_position
        current_position += steps * direction
        end = current_position

        sections.append((start, end))

    vertices = []
    border_size = 0

    for c_range in sections:
        vertices.append(c_range[0])
        border_size += abs(c_range[1] - c_range[0])

    return shoelace_formula(vertices) + (border_size / 2) + 1


if __name__ == '__main__':
    print(solution(1))  # 35401           |  0.00055s  |  0.00046s
    print(solution(2))  # 48020869073824  |  0.00075s  |  0.00064s
