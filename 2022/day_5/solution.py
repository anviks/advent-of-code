"""Day 5."""


def part_1(filename: str):
    """Part 1."""
    with open(filename) as file:
        content = file.read()
    crates = content.split("\n\n")[0]
    instructions = content.split("\n\n")[1]
    stacks = [[], [], [], [], [], [], [], [], []]
    for row in crates.split("\n"):
        for i in range(1, 34, 4):
            if i < len(row) and row[i] != " ":
                stacks[i // 4].append(row[i])
    for stack in stacks:
        stack.pop()
        stack.reverse()
    for line in instructions.split("\n"):
        words = line.split()
        for i in range(int(words[1])):
            stacks[int(words[5]) - 1].append(stacks[int(words[3]) - 1].pop())
    last_crates = ""
    for stack in stacks:
        last_crates += stack[-1]
    return last_crates


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read()
    crates = content.split("\n\n")[0]
    instructions = content.split("\n\n")[1]
    stacks = [[], [], [], [], [], [], [], [], []]
    for row in crates.split("\n"):
        for i in range(1, 34, 4):
            if i < len(row) and row[i] != " ":
                stacks[i // 4].append(row[i])
    for stack in stacks:
        stack.pop()
        stack.reverse()
    for line in instructions.split("\n"):
        words = line.split()
        stacks[int(words[5]) - 1] += stacks[int(words[3]) - 1][-int(words[1]):]
        stacks[int(words[3]) - 1] = stacks[int(words[3]) - 1][:-int(words[1])]
    last_crates = ""
    for stack in stacks:
        last_crates += stack[-1]
    return last_crates


if __name__ == '__main__':
    print(part_1("data.txt"))
    print(part_2("data.txt"))
