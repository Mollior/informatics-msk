b = {}
for x in input().split():
    if x in b:
        print('YES')
    else:
        print('NO')
        b[x] = True
