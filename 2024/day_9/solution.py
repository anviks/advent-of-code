from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('',), int)
data = [data[i - 2] + (1 - i % 2) * i * .5j for i in range(2, len(data) + 2)]
data1 = data.copy()
data2 = data.copy()


@stopwatch
def part1():
    l, r = 1, len(data1) - 1

    while l < len(data1) and r > 0:
        assert data1[l].imag == 0
        if data1[r].real <= data1[l].real:
            data1[l] -= data1[r].real
            data1.insert(l, data1[r])
            data1.pop()
            data1.pop()
            r -= 1
            l += 1
        else:
            data1[l] += data1[r].imag * 1j
            data1[r] -= data1[l].real
            l += 2

    pos = 0
    checksum = 0

    for n in data:
        for _ in range(int(n.real)):
            checksum += pos * (n.imag - 1)
            pos += 1

    return int(checksum)


@stopwatch
def part2():
    l, r = 1, len(data2) - 1

    while r > 0:
        l = 1

        while data2[r].imag == 0:
            r -= 1

        while l < len(data2) and not (data2[l].imag == 0 and data2[l].real >= data2[r].real):
            l += 1

        if l < len(data2) and l < r:
            data2[l] -= data2[r].real
            data2[r - 1] += data2[r].real
            data2.insert(l, data2.pop(r))

        r -= 1

    pos = 0
    checksum = 0

    for n in data2:
        for _ in range(int(n.real)):
            if n.imag != 0:
                checksum += pos * (n.imag - 1)
            pos += 1

    return int(checksum)


if __name__ == '__main__':
    print(part1())  # 15996424901065    |   0.037 seconds
    print(part2())  # 6478232739671     |   36.76 seconds
