import time

from utils_anviks import read_file


@read_file(sep=",", _class=int)
def solution(data: list, part: int):
    """
    Python list can store 536,870,912 elements on a 32-bit system.

    Sample answer for part one was 5,934.
    My answer for part one was 391,888.

    Sample answer for part two was 26,984,457,539.
    My answer for part two was ?.
    """
    fish = {k: 0 for k in range(9)}

    data = list(map(int, data))

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
    start = time.perf_counter()
    print(solution(1))
    print(time.perf_counter() - start)
    print(solution(2))

    # for i in range(days):
    #     for j in range(len(data)):
    #         data[j] -= 1
    #         if data[j] < 0:
    #             data[j] = 6
    #             data.append(8)

    # for i in range(days // 6):
    #     for j in range(len(data)):
    #         if data[j] < 0:
    #             data[j] += 7
    #             data.append(data[j] + 2)


    #     first_cycle_fish = 0
    #     rest_of_the_fish = 300
    #     for i in range(1, days + 1):
    #         # for j in range(len(data)):
    #         #     if i % 6 == 0:
    #         #         first_cycle_fish += 1
    #         #     if i % 8 == 0:
    #         #         rest_of_the_fish += 1
    #
    #         if i % 6 == 0:
    #             first_cycle_fish += rest_of_the_fish
    #         if i % 8 == 0:
    #             rest_of_the_fish += first_cycle_fish
    #
    #     print(first_cycle_fish + rest_of_the_fish)



    #     for i in range(days):
    #         temp = fish[0]
    #         for key in range(8):
    #             fish[key] = fish[key + 1]
    #         fish[8] = temp
    #         fish[6] += temp
    #
    # 0.0002918001264333725 sec



