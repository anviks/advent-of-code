"""AOC day 4."""


def solution(filename: str, part: int):
    """AOC day 4 solution."""
    with open(filename, encoding="utf-8") as file:
        content = file.read().split("\n\n")

    nums = list(map(int, content[0].split(",")))
    content.pop(0)
    boards = [content[i].split("\n") for i in range(len(content))]
    boards_int = []

    for board in boards:
        boards_int.append([])
        for line in board:
            line = line.replace("  ", " ")
            if line[0] == " ":
                line = line[1:]
            line_int = list(map(int, line.split(" ")))
            boards_int[-1].append(line_int)

    for num in nums:
        if num == 77:
            pass
        for board in boards_int:
            if board == [[50, -1, 68, -1, -1], [-1, 12, -1, -1, -1], [28, -1, -1, 30, -1], [41, 51, 15, 27, 97], [67, 70, 14, 77, 86]]:
                pass
            for row in board:
                while num in row:
                    row: list
                    row.insert(row.index(num), -1)
                    row.remove(num)

            for i in range(len(board)):
                if set(board[i]) != {-1}\
                        and not (board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1):
                    continue

                if part == 2 and [len(b) > 0 for b in boards_int].count(True) > 1:
                    index = boards_int.index(board)
                    boards_int[index] = []
                    break

                return num * (sum(board[0]) + sum(board[1]) + sum(board[2]) + sum(board[3]) + sum(board[4])
                              + board[0].count(-1) + board[1].count(-1)
                              + board[2].count(-1) + board[3].count(-1) + board[4].count(-1))



if __name__ == '__main__':
    print(solution("data.txt", 1))
    print(solution("data.txt", 2))
