from itertools import combinations

from utils_anviks import read_data, stopwatch

MIN_POS = 200_000_000_000_000
MAX_POS = 400_000_000_000_000


@read_data('data.txt', sep2=' @ ', sep3=', ', _class=int, auto_annotate=True)
@stopwatch
def solution(data: list[list[list[int]]], part: int):
    acc = 0
    hailstones = []

    for location, velocity in data:
        hailstones.append((location[:2], velocity[:2]))

    pairs = combinations(hailstones, 2)

    for pair in pairs:
        equations = []

        for (location_x, location_y), (velocity_x, velocity_y) in pair:
            # y = slope * x + intercept
            slope = velocity_y / velocity_x
            intercept = location_y - location_x / (1 / slope)

            equations.append((slope, intercept))

        (slope_1, intercept_1), (slope_2, intercept_2) = equations

        # If the slopes are equal, then the lines are parallel and won't meet.
        if slope_1 == slope_2:
            continue

        meet_x = (intercept_2 - intercept_1) / (slope_1 - slope_2)
        meet_y = meet_x * slope_1 + intercept_1

        for (initial_x, _), (velocity_x, _) in pair:
            # If the meet coordinate is larger than the initial coordinate, and the velocity is negative (or vice versa),
            # then the meet point would be behind the initial point, thus it won't be counted.
            if (meet_x - initial_x) * velocity_x < 0:
                break
        else:
            if MIN_POS < meet_x < MAX_POS and MIN_POS < meet_y < MAX_POS:
                acc += 1

    return acc


if __name__ == '__main__':
    print(solution(1))  # 18651
    print(solution(2))
