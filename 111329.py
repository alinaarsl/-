with open('text.txt') as f:
    for text in reversed(f.readlines()):
        print(text.strip( ' \n ' ))
