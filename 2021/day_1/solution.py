from utils_anviks import parse_file_content


def solution(part: int) -> int:
    content = parse_file_content('data.txt', ('\n',), int)

    larger = 0

    if part == 1:
        for i in range(1, len(content)):
            if content[i] > content[i - 1]:
                larger += 1
    else:
        for i in range(3, len(content)):
            if sum(content[i - 2: i + 1]) > sum(content[i - 3:i]):
                larger += 1

    return larger


if __name__ == '__main__':
    print(solution(1))  # 1553
    print(solution(2))  # 1597
