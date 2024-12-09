INPUT_FILE = 'data.txt'
print((p := __import__('utils_anviks').parse_file_content, re := __import__('re'), data := p(INPUT_FILE, (), str), mu := lambda s: sum(int(m.group(1)) * int(m.group(2)) for m in re.finditer(r'mul\((\d{,3}),(\d{,3})\)', s)), 'Part 1: ')[-1], mu(data), '\nPart 2: ', mu(re.sub(r'don\'t\(\).*?(?:do\(\)|$)', '', data, flags=re.DOTALL)), sep='')
