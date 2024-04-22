def solution(filename: str, part: int) -> int:
    with open(filename) as f:
        content = f.read().split("\n")

    larger = 0

    if part == 1:
        for i in range(1, len(content)):
            if int(content[i]) > int(content[i - 1]):
                larger += 1
    else:
        for i in range(3, len(content)):
            if sum(list(map(int, content[i - 2: i + 1]))) > sum(list(map(int, content[i - 3:i]))):
                larger += 1

    return larger


if __name__ == '__main__':
    print(solution("data.txt", 1))
    print(solution("data.txt", 2))
