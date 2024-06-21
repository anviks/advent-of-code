import re
from collections import defaultdict

from utils_anviks import parse_file_content, stopwatch


@stopwatch
def solution(part: int):
    data = parse_file_content('data.txt', ('\n', '|'), str)
    
    # Points in part 1
    total = 0
    cards = defaultdict(lambda: 1)
    card_number = 0

    for line in data:
        card_number += 1
        half1, half2 = line
        winning_numbers = set(re.findall(r"(\d+) +", half1))
        my_numbers = set(re.findall(r" +(\d+)", half2))
        intersection = winning_numbers.intersection(my_numbers)

        if part == 1:
            if (amount := len(intersection)) > 0:
                total += 2 ** (amount - 1)
        else:
            for i in range(1, len(intersection) + 1):
                cards[card_number + i] += cards[card_number]

    if part == 1:
        return total
    return sum(cards.values())


if __name__ == '__main__':
    print(solution(1))  # 22897
    print(solution(2))  # 5095824
