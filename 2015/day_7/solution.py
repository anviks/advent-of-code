from utils_anviks import parse_file_content, parse_string, stopwatch
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, (), str)
data = (data.lower()
        .replace('lshift', '<<')
        .replace('rshift', '>>')
        .replace('or', '|')
        .replace('and', '&')
        .replace('not', '~')
        .replace('is', 'is_')
        .replace('in', 'in_')
        .replace('as', 'as_')
        .replace('if', 'if_'))
data = parse_string(data, ('\n', ' -> '), str)


@stopwatch
def part1():
    gates = data.copy()
    loc = locals()
    while gates:
        for i in range(len(gates) - 1, -1, -1):
            op, var = gates[i]
            try:
                exec(f'{var} = {op} % 65536', globals(), loc)
            except NameError:
                continue
            gates.pop(i)
    return loc['a']


@stopwatch
def part2(p1):
    gates = data.copy()
    loc = locals()
    loc['b'] = p1
    while gates:
        for i in range(len(gates) - 1, -1, -1):
            op, var = gates[i]
            if var != 'b':
                try:
                    exec(f'{var} = {op} % 65536', globals(), loc)
                except NameError:
                    continue
            gates.pop(i)
    return loc['a']


if __name__ == '__main__':
    print(a := part1())  # 46065    | 0.218 seconds
    print(part2(a))      # 14134    | 0.223 seconds
