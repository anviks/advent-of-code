from utils_anviks import read_file


@read_file('data.txt')
def solution(data, part: int):
    return data


if __name__ == '__main__':
    print(solution(1))
    print(solution(2))
