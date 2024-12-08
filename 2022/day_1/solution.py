"""Day 1."""


def ordered_sum_list(filename: str):
    """Sum list."""
    with open(filename, "r") as data:
        content = data.read()
    content_list = content.split("\n\n")
    content_list = list(map(lambda x: x.split("\n"), content_list))
    for i in range(len(content_list)):
        content_list[i] = sum(list(map(int, content_list[i])))
    print(content_list)
    content_list.sort(reverse=True)
    return content_list


def part_1(filename: str):
    """Part 1."""
    return ordered_sum_list(filename)[0]


def part_2(filename: str):
    """Part 2."""
    return sum(ordered_sum_list(filename)[:3])


if __name__ == '__main__':
    # TODO: Wrong answers?
    print(part_1("data.txt"))  # 68442
    print(part_2("data.txt"))  # 204837
