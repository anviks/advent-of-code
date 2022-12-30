"""Day 8."""


def day_8(filename: str, part: int):
    """Day 8."""
    visible = 0
    with open(filename) as file:
        content = file.read().split("\n")
    content = list(map(list, content))
    highest_scenic_score = 0
    for x, row in enumerate(content):
        for i, tree in enumerate(row):
            if i == 0 or i == 98 or x == 0 or x == 98:
                visible += 1
                continue
            scenic_score_left = 0
            scenic_score_right = 0
            scenic_score_up = 0
            scenic_score_down = 0
            left_free = True
            right_free = True
            down_free = True
            up_free = True
            for y in content[x][i - 1::-1]:
                scenic_score_left += 1
                if int(y) >= int(tree):
                    left_free = False
                    break
            for y in content[x][i + 1:]:
                scenic_score_right += 1
                if int(y) >= int(tree):
                    right_free = False
                    break
            for li in content[x - 1::-1]:
                for y in li[i]:
                    if up_free:
                        scenic_score_up += 1
                    if int(y) >= int(tree):
                        up_free = False
                        break
            for li in content[x + 1:]:
                for y in li[i]:
                    if down_free:
                        scenic_score_down += 1
                    if int(y) >= int(tree):
                        down_free = False
                        break
            if left_free or right_free or up_free or down_free:
                visible += 1
            total = scenic_score_left * scenic_score_right * scenic_score_down * scenic_score_up
            highest_scenic_score = total if total > highest_scenic_score else highest_scenic_score
    if part == 1:
        return visible
    return highest_scenic_score


if __name__ == '__main__':
    print(day_8("data.txt", 1))  # 1820
    print(day_8("data.txt", 2))  # 385112
