f = open("input.txt", "r")
s = f.read()
word_dict = dict()
words_ls = list(s.strip().split())
word_set = set(words_ls)
max_occur = 0
max_words = []
for i in range(len(words_ls)):
    if words_ls[i] in word_dict:
        word_dict[words_ls[i]] += 1
        if word_dict[words_ls[i]] > max_occur:
            max_occur = word_dict[words_ls[i]]
    else:
        word_dict[words_ls[i]] = 1
        if 1 > max_occur:
            max_occur = 1

for i in word_set:
    if word_dict[i] == max_occur:
        max_words.append(i)

print(min(max_words))
