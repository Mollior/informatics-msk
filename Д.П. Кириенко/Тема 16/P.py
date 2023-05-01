f = open('input.txt', 'r').read().split()

wc = {}
for x in f:
    if x in wc:
        wc[x] += 1
    else:
        wc[x] = 1

wc_sort =sorted(wc.items(), key=lambda x: (-x[1],x[0]))
for w, c in wc_sort:
    print(w)

