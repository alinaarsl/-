with open('text1.txt', 'rt') as f:
    txt = f.read()
print(txt[::-1][1:].strip('\n'))