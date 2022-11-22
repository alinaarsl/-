word = input("Слово: ")
half1 = word[:int((len(word)+1)/2)]
half2 = word[int((len(word)+1)/2):]
print(half2 + half1)