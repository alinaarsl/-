with open('text.txt', 'r') as f:
    lines = 0
    words = 0
    symbols = 0
    for line in f:
        lines += 1
        words += len(str(line).split())
        symbols+=len(str(line).replace(" ", "").strip('\n').strip('.'))
print(lines)
print(words)
print(symbols)
