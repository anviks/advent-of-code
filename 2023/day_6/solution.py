import math

from utils_anviks import stopwatch


@stopwatch
def solution(data, part: int):
    record_times, distances = data

    if part == 1:
        total = 1

        for time, distance in zip(record_times, distances):
            possibilities = 0
            for t in range(time):
                possibilities += t * (time - t) > distance

            total *= possibilities
    else:
        total = sum(
            (t * (record_times - t) > distances)
            for t in range(record_times)
        )

    return total


def solution_horror(data: list[list[int]] | list[int], part: int):
    record_times, distances = data

    return math.prod(
        sum((t * (time - t) > distance) for t in range(time))
        for time, distance in zip(record_times, distances)
    ) if part == 1 else sum(
        (t * (record_times - t) > distances)
        for t in range(record_times)
    )



if __name__ == '__main__':
    datas = [[35, 69, 68, 87], [213, 1168, 1086, 1248]]
    print(solution(datas, 1))  # 170000
    datas = [35696887, 213116810861248]
    print(solution(datas, 2))  # 20537782
