from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('',), int)
# Example: [(2+1j), (3+0j), (3+2j), (3+0j), (1+3j), (3+0j), (3+4j), (1+0j), (2+5j), ...]
data1 = [data[i - 2] + (1 - i % 2) * i * .5j for i in range(2, len(data) + 2)]
data2 = data1.copy()


def compute_checksum(files):
    pos = checksum = 0
    for n in files:
        for _ in range(int(n.real)):
            if n.imag != 0:
                checksum += pos * (n.imag - 1)
            pos += 1
    return int(checksum)


@stopwatch
def part1():
    l, r = 1, len(data1) - 1

    while l < len(data1) and r > 0:
        assert data1[l].imag == 0
        if data1[r].real <= data1[l].real:  # File fits in the free space
            data1[l] -= data1[r].real  # Subtract size of the file from the size of free space
            data1.insert(l, data1[r])  # Insert the file at the beginning of the free space
            data1.pop()  # Remove the last element (always the file that was inserted)
            data1.pop()  # Remove the last element (always free space, even if its size is 0)
            r -= 1  # Move to the next file
            l += 1  # Due to insertion, remaining free space is shifted to the right
        else:  # File doesn't fit in the free space
            data1[l] += data1[r].imag * 1j  # File at r takes up the entire free space at l, so just add the ID of file to it
            data1[r] -= data1[l].real  # Subtract the size of the free space from the size of the file
            l += 2  # There was no insertion, and free space was used up, so move to the next free space

    return compute_checksum(data1)


@stopwatch
def part2():
    r = len(data2) - 1

    while r > 0:
        l = 1

        # Find the next file from the right
        while r > 0 and data2[r].imag == 0:
            r -= 1

        if r == 0:
            break

        # Find the first free space, where the entire file can fit
        while l < r and not (data2[l].imag == 0 and data2[l].real >= data2[r].real):
            l += 1

        if l < r:
            # Switch the file with the free space
            data2[l] -= data2[r].real
            data2[r - 1] += data2[r].real  # In this part, free space preservation is necessary!
            data2.insert(l, data2.pop(r))

        r -= 1

    return compute_checksum(data2)


if __name__ == '__main__':
    print(part1())  # 6446899523367    |   0.037 seconds
    print(part2())  # 6478232739671    |   16.61 seconds
