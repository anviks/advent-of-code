from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", ""), int)


@stopwatch
def part1():
    output = 0

    for bank in data:
        battery1, battery2 = bank[:2]

        for i in range(2, len(bank)):
            if battery2 > battery1:
                battery1 = battery2
                battery2 = bank[i]
            elif bank[i] > battery2:
                battery2 = bank[i]

        output += battery1 * 10 + battery2

    return output


@stopwatch
def part2():
    output = 0

    for bank in data:
        batteries = bank[:12]

        for i in range(12, len(bank)):
            for j in range(1, 12):
                # If next digit is larger, shift the right half one slot to the right
                if batteries[j - 1] < batteries[j]:
                    for k in range(j, 12):
                        batteries[k - 1] = batteries[k]
                    batteries[11] = bank[i]
                    break
            else:
                if batteries[11] < bank[i]:
                    batteries[11] = bank[i]

        output += int("".join(map(str, batteries)))

    return output


if __name__ == "__main__":
    print(part1())  # 17435             | 0.0009 seconds
    print(part2())  # 163992267694420   | 0.0128 seconds
