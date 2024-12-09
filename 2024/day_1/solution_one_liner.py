INPUT_FILE = 'data.txt'

print((data := list(zip(*(__import__('utils_anviks').parse_file_content(INPUT_FILE, ('\n', '   '), int)))), c := __import__('collections').Counter(data[1]), 'Part 1: ')[-1], sum(abs(a - b) for a, b in (list(zip(*[sorted(a) for a in data])))), '\nPart 2: ', sum(c[n] * n for n in data[0]), sep='')
