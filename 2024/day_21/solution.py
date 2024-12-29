from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file0, ('\n',), str)


def dir_keypad_to_press(res: str):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    pressed = []
    keys = '<v>^A'
    idx = 4

    for to_press in res:
        target = keys.index(to_press)
        while idx != target:
            if idx > target:
                if idx > target + idx % 3:
                    idx -= 2
                    pressed.append('v')
                else:
                    idx -= 1
                    pressed.append('<')
            else:
                if target > idx + target % 3 and idx != 0:
                    idx += 2
                    pressed.append('^')
                else:
                    idx += 1
                    pressed.append('>')
        pressed.append('A')

    print(''.join(pressed))
    return ''.join(pressed)


def num_keypad_to_press(res: str):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    pressed = []
    keys = '0A123456789'
    idx = 1

    for to_press in res:
        target = keys.index(to_press)
        while idx != target:
            if idx > target:
                if idx > target + (idx + 1) % 3 and idx != 2:
                    idx -= 3
                    pressed.append('v')
                else:
                    idx -= 1
                    pressed.append('<')
            else:
                if target > idx + (target + 1) % 3:
                    idx += 3
                    pressed.append('^')
                else:
                    idx += 1
                    pressed.append('>')
        pressed.append('A')

    print(''.join(pressed))
    return ''.join(pressed)



def part1():
    acc = 0
    for code in data:
        result = num_keypad_to_press(code)
        print(len(result))
        for _ in range(2):
            result = dir_keypad_to_press(result)
            print(len(result))
        acc += len(result) * int(code[:-1])
    return acc


def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
