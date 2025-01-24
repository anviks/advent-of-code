from utils_anviks import parse_file_content, parse_string, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, (), str).replace(', ', ',')
data = parse_string(data, ('\n', ' '), str)


@stopwatch
def solve(part: int):
    registers = {'a': part == 2, 'b': 0}
    i = 0

    while i < len(data):
        cmd, arg = data[i]
        if cmd == 'hlf':
            registers[arg] //= 2
        elif cmd == 'tpl':
            registers[arg] *= 3
        elif cmd == 'inc':
            registers[arg] += 1
        elif cmd == 'jmp':
            i += int(arg) - 1
        elif cmd in ['jie', 'jio']:
            reg, offset = arg.split(',')
            if (cmd == 'jie' and registers[reg] % 2 == 0
                    or cmd == 'jio' and registers[reg] == 1):
                i += int(offset) - 1
        i += 1

    return registers['b']


if __name__ == '__main__':
    print(solve(1))  # 170  | 0.00028 seconds
    print(solve(2))  # 247  | 0.00038 seconds
