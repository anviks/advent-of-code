from operator import and_, or_, xor

from utils_anviks import parse_file_content, parse_string, stopwatch


def parse_file(file: str):
    w, g = parse_file_content(file, ('\n\n',), str)
    w = parse_string(w, ('\n', ': '), str)
    wires = {k: bool(int(v)) for k, v in w}
    gates: list[list[list[str | bool]]] = parse_string(g, ('\n', ' -> ', ' '), str)
    return wires, gates


@stopwatch
def part1():
    wires, gates = parse_file('data.txt')
    operations = {'XOR': xor, 'OR': or_, 'AND': and_}

    while sum(1 for key in wires.keys() if key[0] == 'z') < 45:
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
    _, gates = parse_file('data2.txt')
    gates: set[tuple[tuple[str, str, str], tuple[str]]] = {tuple(tuple(g) for g in gate) for gate in gates}  # type: ignore
    gates_map = {tuple(op): value[0] for op, value in gates}
    expected = set()

    def get_frags(gate: tuple[str, str, str]):
        """
        Get permutations of the gate, but only those, that are next to each other.
        Meaning, if the gate is (('abc, 'XOR', 'def'), ...),
        the result will be {('abc', 'XOR'), ('XOR', 'def'), ('def', 'XOR'), ('XOR', 'abc')}
        """
        op = gate
        return {op[:2], op[1:], op[:0:-1], op[1::-1]}

    def add_gate(operation: tuple[str, str, str]):
        if None in operation:
            return None

        if operation[0][0] == 'z' or operation[2][0] == 'z':
            raise ValueError(' '.join(operation), 'z can never be an argument, which means it\'s misplaced as a result')

        if operation in gates_map:
            gate = operation
        else:
            gate = operation[::-1]

        if gate not in gates_map:
            diff_frags = {frag for frag in get_frags(gate)}
            should_be = {name for g in gates if get_frags(g[0]) & diff_frags for name in g[0]}
            gates_to_swap = {name for frag in diff_frags for name in frag} ^ should_be
            raise ValueError(f'Gates to swap: {gates_to_swap}')

        gate_name = gates_map[gate]
        expected.add((gate, (gate_name,)))
        return gate_name

    add_gate(('x00', 'XOR', 'y00'))
    out = add_gate(('x00', 'AND', 'y00'))

    for i in range(1, 45):
        x = f'x{i:02}'
        y = f'y{i:02}'

        tl = add_gate((x, 'XOR', y))
        bl = add_gate((x, 'AND', y))
        add_gate((tl, 'XOR', out))
        mid = add_gate((tl, 'AND', out))
        out = add_gate((mid, 'OR', bl))


if __name__ == '__main__':
    print(part1())  # 49574189473968    | 0.0026 seconds
    print(part2())  # ckb,kbs,ksv,nbd,tqq,z06,z20,z39
    # z06 <=> ksv, kbs <=> nbd, tqq <=> z20, ckb <=> z39
