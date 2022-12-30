"""Day 5."""


def part_1(filename: str):
    """Part 1."""
    with open(filename) as file:
        content = file.read()
    crates = content.split("\n\n")[0]
    instructions = content.split("\n\n")[1]
    for i in range(1, 10):
        exec(f"stack_{i} = []", globals())
    for row in crates.split("\n"):
        if 1 < len(row) and row[1] != " ":
            stack_1.append(row[1])
        if 5 < len(row) and row[5] != " ":
            stack_2.append(row[5])
        if 9 < len(row) and row[9] != " ":
            stack_3.append(row[9])
        if 13 < len(row) and row[13] != " ":
            stack_4.append(row[13])
        if 17 < len(row) and row[17] != " ":
            stack_5.append(row[17])
        if 21 < len(row) and row[21] != " ":
            stack_6.append(row[21])
        if 25 < len(row) and row[25] != " ":
            stack_7.append(row[25])
        if 29 < len(row) and row[29] != " ":
            stack_8.append(row[29])
        if 33 < len(row) and row[33] != " ":
            stack_9.append(row[33])
    for i in range(1, 10):
        exec(f"stack_{i}.pop()")
        exec(f"stack_{i}.reverse()")
    for line in instructions.split("\n"):
        words = line.split()
        for i in range(int(words[1])):
            exec(f"stack_{words[5]}.append(stack_{words[3]}.pop())")
    exec(f"temp = \"\"", globals())
    for i in range(1, 10):
        exec(f"temp += stack_{i}[-1]", globals())
    return temp


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read()
    crates = content.split("\n\n")[0]
    instructions = content.split("\n\n")[1]
    for i in range(1, 10):
        exec(f"stack_{i} = []", globals())
    for row in crates.split("\n"):
        if 1 < len(row) and row[1] != " ":
            stack_1.append(row[1])
        if 5 < len(row) and row[5] != " ":
            stack_2.append(row[5])
        if 9 < len(row) and row[9] != " ":
            stack_3.append(row[9])
        if 13 < len(row) and row[13] != " ":
            stack_4.append(row[13])
        if 17 < len(row) and row[17] != " ":
            stack_5.append(row[17])
        if 21 < len(row) and row[21] != " ":
            stack_6.append(row[21])
        if 25 < len(row) and row[25] != " ":
            stack_7.append(row[25])
        if 29 < len(row) and row[29] != " ":
            stack_8.append(row[29])
        if 33 < len(row) and row[33] != " ":
            stack_9.append(row[33])
    for i in range(1, 10):
        exec(f"stack_{i}.pop()")
        exec(f"stack_{i}.reverse()")
    for line in instructions.split("\n"):
        words = line.split()
        exec(f"stack_{words[5]} += stack_{words[3]}[-{words[1]}:]")
        exec(f"stack_{words[3]} = stack_{words[3]}[:-{words[1]}]")
    exec(f"temp = \"\"", globals())
    for i in range(1, 10):
        exec(f"temp += stack_{i}[-1]", globals())
        exec(f"print(stack_{i}[-1])")
    return temp


if __name__ == '__main__':
    print(part_1("data.txt"))
    print(part_2("data.txt"))
