"""Day 4."""


def part_1(filename: str):
    """Part 1."""
    with open(filename) as file:
        content = file.read().split("\n")
    count = 0
    for row in content:
        section = row.split(",")
        if int(section[0].split("-")[0]) <= int(section[1].split("-")[0]) and \
                int(section[0].split("-")[1]) >= int(section[1].split("-")[1]) or int(section[0].split("-")[0]) >= \
                int(section[1].split("-")[0]) and int(section[0].split("-")[1]) <= int(section[1].split("-")[1]):
            count += 1
    return count


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read().split("\n")
    count = 0
    for row in content:
        section = row.split(",")
        if int(section[1].split("-")[1]) >= int(section[0].split("-")[1]) >= int(section[1].split("-")[0]) or \
                int(section[0].split("-")[1]) >= int(section[1].split("-")[1]) >= int(section[0].split("-")[0]):
            count += 1
    return count


if __name__ == '__main__':
    print(part_1("data.txt"))  # 433
    print(part_2("data.txt"))  # 852
