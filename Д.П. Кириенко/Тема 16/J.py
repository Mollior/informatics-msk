n, k = map(int, input().split())

set_days = set()
weekends = set(range(6,n,7)) | set(range(7,n,7))
for i in range(k):
    a, b = map(int, input().split())
    day = a
    while day <= n:
        if day % 7 != 6 and day % 7 != 0:
            set_days.add(day)
        day += b
print(len(set_days))
