k = list(map(int, input().split()))
n = set()
m =set()
for x in range(k[0]):
    n.add(int(input()))
for i in range(k[1]):
    m.add(int(input()))
ob = n & m
ostn = n - ob
ostm = m - ob
print(len(ob))
print(*sorted(ob), sep = " ")
print(len(ostn))
print(*sorted(ostn), sep = " ")
print(len(ostm))
print(*sorted(ostm), sep = " ")
