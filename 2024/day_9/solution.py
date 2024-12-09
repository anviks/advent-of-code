from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file0, ('',), int)
# Example: [(2+1j), (3+0j), (3+2j), (3+0j), (1+3j), (3+0j), (3+4j), (1+0j), (2+5j), (1+0j), (4+6j), (1+0j), (4+7j), (1+0j), (3+8j), (1+0j), (4+9j), 0j, (2+10j)]
data1 = [data[i] + (i % 2 == 0) * (i + 2) * .5j for i in range(len(data))]
data2 = data1.copy()


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

    for n in data1:
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
