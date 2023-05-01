f = input().split()

wc = {}

for x in f:
    if x in wc:
        wc[x] += 1
    else:
        wc[x] = 1
maxc = 0
maxw = []
for w, c in wc.items():
    if c > maxc:
        maxc = c
        maxw = [w]
    elif c == maxc:
        maxw.append(w)
maxw.sort()
print(maxw[0])
#wc_sort = dict(sorted(wc.items()))
#print(max(wc_sort, key=wc_sort.get))
