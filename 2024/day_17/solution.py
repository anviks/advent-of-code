from utils_anviks import stopwatch

program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]


def execute(a, b, c):
    pointer = 0
    result = []

    combo = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: lambda: a,
        5: lambda: b,
        6: lambda: c,
    }

    def i0(x): nonlocal a; a >>= combo[x]()
    def i1(x): nonlocal b; b ^= x
    def i2(x): nonlocal b; b = combo[x]() % 8
    def i3(x):
        if a == 0: return
        nonlocal pointer
        pointer = x - 2
    def i4(x): nonlocal b; b ^= c
    def i5(x): return combo[x]() % 8
    def i6(x): nonlocal b; b = a >> combo[x]()
    def i7(x): nonlocal c; c = a >> combo[x]()

    while pointer < len(program):
        opcode, operand = program[pointer:pointer + 2]
        out = locals()[f'i{opcode}'](operand)
        if out is not None:
            result.append(out)
        pointer += 2

    return result


@stopwatch
def part1():
    return ','.join(map(str, execute(30344604, 0, 0)))


@stopwatch
def part2():
    queue = [(1, 0)]
    for i, reg_a in queue:
        for a in range(reg_a, reg_a + 8):
            if execute(a, 0, 0) == program[-i:]:
                if i == len(program):
                    return a
                queue.append((i + 1, a * 8))


if __name__ == '__main__':
    print(part1())  # 4,3,2,6,4,5,3,2,4     | 0.00013 seconds
    print(part2())  # 164540892147389       | 0.05 seconds
