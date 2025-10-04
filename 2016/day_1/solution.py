from pathlib import Path
from utils_anviks import parse_file_content, stopwatch, Cell

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (", ",), str)


@stopwatch
def part1():
    coord, cur_dir = 0, -1

    for instruction in data:
        direction, length = instruction[0], int(instruction[1:])

        if direction == "L":
            cur_dir /= -1j
        elif direction == "R":
            cur_dir /= 1j
        else:
            raise ValueError(f"Unknown direction: {direction}")

        coord += length * cur_dir

    return int(abs(coord.real) + abs(coord.imag))


@stopwatch
def part2():
    coord, cur_dir = 0, -1
    visited = set()

    for instruction in data:
        direction, length = instruction[0], int(instruction[1:])

        if direction == "L":
            cur_dir /= -1j
        elif direction == "R":
            cur_dir /= 1j
        else:
            raise ValueError(f"Unknown direction: {direction}")

        for _ in range(length):
            coord += cur_dir

            if coord in visited:
                return int(abs(coord.real) + abs(coord.imag))
            
            visited.add(coord)


if __name__ == "__main__":
    print(part1())  # 300
    print(part2())  # 159
