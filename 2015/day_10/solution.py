from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), str)


def get_chunks(digits: str):
    chunks = []
    l = r = 0
    while r < len(digits):
        while r < len(digits) and digits[r] == digits[l]:
            r += 1
        chunks.append(digits[l:r])
        l = r
    return chunks


def look_and_say(digits: str):
    chunks = get_chunks(digits)
    digits = ''
    for chunk in chunks:
        digits += str(len(chunk)) + chunk[0]
    return digits


@stopwatch
def part1():
    result = data
    for _ in range(40):
        result = look_and_say(result)
    return len(result)


@stopwatch
def part2():
    result = data
    for _ in range(50):
        result = look_and_say(result)
    return len(result)


if __name__ == '__main__':
    print(part1())  # 492982    | 0.61 seconds
    print(part2())  # 6989950   | 11.57 seconds
