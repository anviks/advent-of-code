from utils_anviks import parse_file_content, stopwatch, parse_string
from operator import or_, xor, and_

file = 'data.txt'
file0 = 'example.txt'
w, g = parse_file_content(file, ('\n\n',), str)
w = parse_string(w, ('\n', ': '), str)
wires = {k: bool(int(v)) for k, v in w}
gates: list[list[list[str | bool]]] = parse_string(g, ('\n', ' -> ', ' '), str)
operations = {'XOR': xor, 'OR': or_, 'AND': and_}
z_count = sum(1 for g in gates if g[1][0][0] == 'z')

print(wires)
print(gates)

@stopwatch
def part1():
    while sum(1 for key in wires.keys() if key[0] == 'z') < z_count:
        for gate in gates:
            (l, op, r), (result,) = gate
            if l in wires:
                l = gate[0][0] = wires[l]
            if r in wires:
                r = gate[0][2] = wires[r]
            if isinstance(l, bool) and isinstance(r, bool):
                wires[result] = operations[op](l, r)

    z_wires = sorted([(k, v) for k, v in wires.items() if k[0] == 'z'], key=lambda kv: int(kv[0][1:]))
    acc = 0
    for i, (_, value) in enumerate(z_wires):
        if value:
            acc |= 1 << i
    return acc


def part2():
    pass



if __name__ == '__main__':
    print(part1())  # 49574189473968    | 0.0026 seconds
    print(part2())
