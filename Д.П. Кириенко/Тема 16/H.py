n = int(input())
possible = set(range(1, n + 1))
qest = set()
ans = []
get_input = True
while get_input:
    tmp = input()
    if tmp == "HELP":
        get_input = False
    else:
        s = set(map(int, tmp.split()))
        if len(s.intersection(possible)) <= 0.5 * len(possible):
            ans.append("NO")
            possible -= s
        else:
            ans.append("YES")
            possible &= s

for i in ans:
    print(i)
for i in sorted(possible):
    print(i, end=" ")
