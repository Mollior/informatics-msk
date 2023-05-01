p = []
pi = 0
for x in range(100):
    if x % 2 != 0:
        p.append(x)
    if len(p) == 10:
        break
for c in range(len(p)):
    if c % 2 == 0:
        pi += 4/p[c] 
    else:
        pi -= 4/p[c]
print(pi)
