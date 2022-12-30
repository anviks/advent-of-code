def sum_lines(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    sums = [0]
    for line in lines:
        if line == '':
            sums.append(0)
        else:
            sums[-1] += int(line)
    return sums


if __name__ == '__main__':
    # print(sum_lines("data.txt"))
    with open("data.txt") as f:
        print(f.read(3))
