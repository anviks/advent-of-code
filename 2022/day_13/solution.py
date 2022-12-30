"""Day 13."""


def compare_packets(left, right):
    """Compare two packets."""
    if type(left) is int and type(right) is int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1
    elif type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            comp = compare_packets(left[i], right[i])
            if comp == -1:
                return -1
            elif comp == 1:
                return 1
        if len(left) < len(right):
            return 1
        elif len(right) < len(left):
            return -1
        else:
            return 0
    elif type(left) is list and type(right) is int:
        return compare_packets(left, [right])
    else:
        return compare_packets([left], right)


def packets(filename: str, part: int):
    """Day 13."""
    indices = 0
    pairs2 = []
    with open(filename) as f:
        pairs = f.read().split("\n\n")
    for pair in pairs:
        left, right = pair.split("\n")
        left, right = eval(left), eval(right)
        pairs2.append(left)
        pairs2.append(right)
        if compare_packets(left, right) == 1:
            indices += pairs.index(pair) + 1
    if part == 1:
        return indices
    index_2 = 1
    index_6 = 2
    for pair in pairs2:
        index_2 += 1 if compare_packets(pair, [[2]]) == 1 else 0
        index_6 += 1 if compare_packets(pair, [[6]]) == 1 else 0
    return index_2 * index_6


if __name__ == '__main__':
    print(packets("data.txt", 1))
    print(packets("data.txt", 2))
