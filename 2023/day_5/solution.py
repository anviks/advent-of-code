import sys

from utils_anviks import read_file, stopwatch


def apply_mappings(seeds: list[int], mappings: list[list[tuple[int, int, int]]]) -> list[int]:
    locations = []

    for item in seeds:
        for map_set in mappings:
            for destination, source, length in map_set:
                if source <= item < source + length:
                    item = destination + item - source
                    break

        locations.append(item)

    return locations


def parse_mappings(data: list[str]) -> list[list[tuple[int, int, int]]]:
    mappings = []
    for row in data:
        if "map" in row:
            mappings.append([])
        elif row:
            mappings[-1].append(tuple(map(int, row.split(" "))))
    return mappings


@read_file('data.txt')
@stopwatch
def solution(data: list[str], part: int) -> int:
    return solve_part_one(data) if part == 1 else solve_part_two(data)


def solve_part_one(data: list[str]) -> int:
    seeds = list(map(int, data[0].split(" ")[1:]))
    data.pop(0)

    mappings = parse_mappings(data)
    locations = apply_mappings(seeds, mappings)

    return min(locations)

def solve_part_two(data: list[str]) -> int:
    seeds_line = list(map(int, data[0].split(" ")[1:]))
    seed_ranges = []
    for i in range(0, len(seeds_line), 2):
        seed_ranges.append(range(seeds_line[i], seeds_line[i + 1] + seeds_line[i]))

    data.pop(0)

    mappings = parse_mappings(data)

    smallest = sys.maxsize
    for s_range in seed_ranges:
        ranges = [s_range]

        for map_set in mappings:
            if map_set == [(45, 77, 23), (81, 45, 19), (68, 64, 13)]:
                pass
            new_ranges = []
            while ranges:
                current_range = ranges.pop()

                for map_dest_start, map_src_start, map_length in map_set:
                    # Exclusive
                    map_src_end = map_src_start + map_length

                    # New range must be fully contained by both the current range and the current mapping
                    new_range_start = max(map_src_start, current_range.start)
                    new_range_end = min(map_src_end, current_range.stop)

                    if new_range_start < new_range_end:
                        offset = map_dest_start - map_src_start
                        new_range = range(new_range_start + offset, new_range_end + offset)
                        new_ranges.append(new_range)

                        # If the new range is smaller than the current range, split the current range
                        # and add the parts that are not in the new range to the ranges list to be processed
                        # in the next iterations

                        if new_range_start > current_range.start:
                            ranges.append(range(current_range.start, new_range_start))

                        if new_range_end < current_range.stop:
                            ranges.append(range(new_range_end, current_range.stop))

                        break
                else:
                    # No mapping found, keep the range as is
                    new_ranges.append(current_range)

            ranges = new_ranges

        # Find the smallest number in the ranges
        smallest = min(smallest, min([r.start for r in ranges]))

    return smallest


if __name__ == '__main__':
    print(solution(1))  # 318728750
    print(solution(2))  # 37384986
