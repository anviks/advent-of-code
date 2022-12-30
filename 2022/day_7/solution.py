"""Day 7."""


def day_7(filename: str, part: int):
    """Day 7."""
    with open(filename) as file:
        content = file.read().split("\n")
    directory = []  # Shows the directory that the loop is currently in.
    directory_sizes = {}  # Absolute paths of folders and their total sizes.
    for line in content:
        line = line.split(" ")  # Takes a line as a list.
        if line[0] == "$" and line[1] == "cd":  # Checks for the cd command as no other command requires an action.
            if line[2] == "..":
                directory.pop()  # If the command is "$ cd ..", then exit the folder.
            else:
                directory.append(line[2])  # Otherwise, enter the mentioned folder.
        if line[0].isdigit():  # Checks if the line is a file (with its first element being its size).
            for i in range(len(directory)):
                directory_sizes["/".join(directory[:i + 1])] = \
                    directory_sizes.get("/".join(directory[:i + 1]), 0) + int(line[0])
                # Adds the file size to the total size of each folder.
    if part == 1:
        return sum(list(filter(lambda x: x <= 100_000, list(map(lambda x: directory_sizes[x], directory_sizes)))))
        # Return the size sum of every directory, that has 100k worth of files or less in them.
    return min(list(filter(lambda x: x >= 30_000_000 - (70_000_000 - directory_sizes["/"]), directory_sizes.values())))
    # Knowing that the total usable space of the computer is 70M units and 30M is needed to be available, return the
    # size of the smallest folder, that could free up enough space.


if __name__ == '__main__':
    print(day_7("data.txt", 1))  # 1297683
    print(day_7("data.txt", 2))  # 5756764
