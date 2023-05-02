words = dict()

n = int(input())
for i in range(n):
    tmp = input()
    tmp_key = tmp.lower()
    if tmp_key in words:
        words[tmp.lower()].append(tmp)
    else:
        words[tmp.lower()] = [tmp]

s_words = list(input().split())
n_mistakes = 0
for i in s_words:
    i_check = i.lower()
    n_upper = 0
    for j in i:
        if 64 < ord(j) < 91:
            n_upper += 1
        if n_upper > 1:
            break
    if i_check in words and n_upper == 1:
        if i not in words[i_check]:
            n_mistakes += 1
    elif n_upper != 1:
        n_mistakes += 1

print(n_mistakes)
