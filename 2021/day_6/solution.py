from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution(part: int):
    """
    Python list can store 536,870,912 elements on a 32-bit system.

    Sample answer for part one was 5,934.
    My answer for part one was 391,888.

    Sample answer for part two was 26,984,457,539.
    My answer for part two was 1,754,597,645,339.
    """
    fish = {k: 0 for k in range(9)}
    data = parse_file_content('data.txt', (',',), int)

    for f in data:
        fish[f] += 1

    days = 80 if part == 1 else 256

    for i in range(days):
        temp = fish[0]
        for key in range(8):
            fish[key] = fish[key + 1]
        fish[8] = temp
        fish[6] += temp

    return sum(fish.values())


if __name__ == '__main__':
    print(solution(1))  # 391888
    print(solution(2))  # 1754597645339
