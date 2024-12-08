"""Day 9."""


def day_9(filename: str, part: int):
    """Day 9."""
    with open(filename) as file:
        content = file.read().split("\n")
    positions_visited = []
    head_pos = [0, 0]
    tail_pos = [0, 0]
    for movement in content:
        direction = movement.split(" ")[0]
        for i in range(int(movement.split(" ")[-1])):
            if direction == "R":
                head_pos[0] += 1
            elif direction == "L":
                head_pos[0] -= 1
            elif direction == "U":
                head_pos[1] += 1
            else:
                head_pos[1] -= 1
            if head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == 0:
                tail_pos[0] += 1
            elif head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == 0:
                tail_pos[0] -= 1
            elif head_pos[1] - tail_pos[1] == 2 and head_pos[0] - tail_pos[0] == 0:
                tail_pos[1] += 1
            elif head_pos[1] - tail_pos[1] == -2 and head_pos[0] - tail_pos[0] == 0:
                tail_pos[1] -= 1
            elif head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == 1 or \
                    head_pos[0] - tail_pos[0] == 1 and head_pos[1] - tail_pos[1] == 2:
                tail_pos[0] += 1
                tail_pos[1] += 1
            elif head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == 1 or \
                    head_pos[0] - tail_pos[0] == -1 and head_pos[1] - tail_pos[1] == 2:
                tail_pos[0] -= 1
                tail_pos[1] += 1
            elif head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == -1 or \
                    head_pos[0] - tail_pos[0] == -1 and head_pos[1] - tail_pos[1] == -2:
                tail_pos[0] -= 1
                tail_pos[1] -= 1
            elif head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == -1 or \
                    head_pos[0] - tail_pos[0] == 1 and head_pos[1] - tail_pos[1] == -2:
                tail_pos[0] += 1
                tail_pos[1] -= 1
            positions_visited.append(tail_pos.copy())
    for array in positions_visited.copy():
        if positions_visited.count(array) > 1:
            positions_visited.remove(array)
    if part == 1:
        return len(positions_visited)


if __name__ == '__main__':
    print(day_9("data.txt", 1))  # 6266
    # TODO: Implement part 2
    print(day_9("data.txt", 2))  # 2369
