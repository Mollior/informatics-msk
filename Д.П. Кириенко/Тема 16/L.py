n = int(input())
synonyms = {}

for x in range(n):
    w1, w2 = input().split()
    synonyms[w1] = w2
    synonyms[w2] = w1
w = input()
print(synonyms[w])
