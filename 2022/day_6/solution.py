"""Day 6."""


def day_6(filename: str, part: int):
    """Day 6."""
    with open(filename) as file:
        content = file.read()
    letters_processed = 0
    marker = ""
    for letter in content:
        if letter in marker:
            marker = ""
        marker += letter
        letters_processed += 1
        if len(marker) == 4 and part == 1:
            break
        elif len(marker) == 14:
            break
    return letters_processed


if __name__ == '__main__':
    print(day_6("data.txt", 1))
    print(day_6("data.txt", 2))
