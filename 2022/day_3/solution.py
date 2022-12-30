"""Day 3."""


def part_1(filename: str):
    """Part 1."""
    with open(filename) as file:
        content = file.read().split("\n")
    priority_sum = 0
    for row in content:
        half_1 = row[:len(row) // 2]
        half_2 = row[len(row) // 2:]
        common_letters = set(half_1).intersection(set(half_2))
        for letter in common_letters:
            if letter.isupper():
                priority_sum += ord(letter) - ord("A") + 27
            else:
                priority_sum += ord(letter) - ord("a") + 1
    return priority_sum


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read().split("\n")
    priority_sum = 0
    for i in range(2, len(content), 3):
        badge = set(content[i]).intersection(set(content[i - 1])).intersection(set(content[i - 2])).pop()
        if badge.isupper():
            priority_sum += ord(badge) - ord("A") + 27
        else:
            priority_sum += ord(badge) - ord("a") + 1
    return priority_sum


if __name__ == '__main__':
    print(part_1("data.txt"))
    print(part_2("data.txt"))
