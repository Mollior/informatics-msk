ns = set(range(1,int(input())+1))
while True:
    ques = input()
    if ques == "HELP":
        break
    ans = input()
    num = set(map(int, ques.split()))
    if ans == "YES":
        ns &= num
    else:
        ns -= num
print(*sorted(ns), sep = " ")