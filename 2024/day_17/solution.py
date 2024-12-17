from utils_anviks import stopwatch

pointer = 0

reg = {
    'A': 30344604,
    'B': 0,
    'C': 0,
}

program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]

combo = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: reg['A'],
    5: lambda: reg['B'],
    6: lambda: reg['C'],
}


def i0(x): reg['A'] >>= combo[x]()
def i1(x): reg['B'] ^= x
def i2(x): reg['B'] = combo[x]() % 8
def i3(x):
    if reg['A'] == 0: return
    global pointer
    pointer = x - 2
def i4(x): reg['B'] ^= reg['C']
def i5(x): return combo[x]() % 8
def i6(x): reg['B'] = reg['A'] >> combo[x]()
def i7(x): reg['C'] = reg['A'] >> combo[x]()


@stopwatch
def part1():
    global pointer
    result = []

    while pointer < len(program):
        opcode, operand = program[pointer:pointer + 2]
        out = globals()[f'i{opcode}'](operand)
        if out is not None:
            result.append(str(out))
        pointer += 2

    return ','.join(result)


def part2():
    pass
    # global pointer
    # result = []
    # iteration = -1
    #
    # while result != program:
    #     result.clear()
    #     pointer = 0
    #     iteration += 1
    #     reg['A'] = iteration
    #
    #     if reg['A'] % 100_000 == 0:
    #         print(reg['A'])
    #
    #     while pointer < len(program):
    #         opcode, operand = program[pointer:pointer + 2]
    #         out = globals()[f'i{opcode}'](operand)
    #         if out is not None:
    #             result.append(str(out))
    #         pointer += 2
    #
    # return reg['A']


if __name__ == '__main__':
    print(part1())
    print(part2())
