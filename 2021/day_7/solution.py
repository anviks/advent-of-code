import time

from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', (',',), int)
    
    if part == 1:
        median = sorted(data)[len(data) // 2]
        return sum(abs(j - median) for j in data)
    else:
        avg = sum(data) // len(data)
        result = 0

        for j in data:
            difference = abs(j - avg)
            result += difference * (difference + 1) / 2

        return int(result)


if __name__ == '__main__':
    print(solution(1))
    print(solution(2))

    #     fuel_consumptions = {}
    #
    #     if part == 1:
    #         for i in range(max(data) + 1):
    #             fuel_consumptions[i] = sum(abs(j - i) for j in data)
    #
    #     return min(fuel_consumptions.values())
    #
    # This: 0.15283969999291003 sec
    # New (median): 0.0004743000026792288 sec