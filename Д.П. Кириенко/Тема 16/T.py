n = int(input()) # количество слов в словаре
dicti = set() # множество слов из словаря
for i in range(n):
    word = input()
    dicti.add(word.lower())

words = input().split()
errors = 0 

for word in words:
    if word.lower() in dicti: 
        accents = set()
        for i in enumerate(word):
            if i.isupper():
                accents.add(i)
        variants = set()
        for accent_pos in accents:
            variant = word[:accent_pos] + word[accent_pos].lower() + word[accent_pos+1:]
            if variant.lower() in dictionary:
                variants.add(variant)
        if not variants:
            errors += 1
    else: 
        accents = 0
        for letter in word:
            if letter.isupper():
                accents += 1
        if accents != 1:
            errors += 1

print(errors)
