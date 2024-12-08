"""AOC day 3."""
from utils_anviks import parse_file_content


def solution(part: int):
    """AOC day 3 solution."""
    content = parse_file_content('data.txt', ('\n',), str)

    gamma_rate = ""
    epsilon_rate = ""
    o2_values = content.copy()
    co2_values = content.copy()

    for order in range(len(content[0])):
        bits = []

        for sequence in content:
            bits.append(sequence[order])

        if bits.count("1") >= bits.count("0"):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    for order in range(len(o2_values[0])):
        bits = []

        for sequence in o2_values:
            bits.append(sequence[order])

        if bits.count("1") >= bits.count("0"):
            o2_values = list(filter(lambda x: x[order] == "1", o2_values))
        else:
            o2_values = list(filter(lambda x: x[order] == "0", o2_values))

    for order in range(len(co2_values[0])):
        bits = []

        for sequence in co2_values:
            bits.append(sequence[order])

        if bits.count("1") >= bits.count("0"):
            co2_values = list(filter(lambda x: x[order] == "0", co2_values))
        else:
            co2_values = list(filter(lambda x: x[order] == "1", co2_values))

        if len(co2_values) == 1:
            break

    if part == 1:
        return int(gamma_rate, 2) * int(epsilon_rate, 2)
    return int(o2_values[0], 2) * int(co2_values[0], 2)


if __name__ == '__main__':
    print(solution(1))  # 4191876
    print(solution(2))  # 3414905
