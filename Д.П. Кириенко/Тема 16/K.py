words_count = {}
words = open('input.txt','r').read().split()
for x in words:
    if x in words_count:
        print(words_count[x], end=' ')
        words_count[x] += 1
    else:
        print(0, end=' ')
        words_count[x] = 1
