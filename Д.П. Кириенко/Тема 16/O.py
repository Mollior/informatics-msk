n = int(input())
out = []
files = {}
for i in range(n):
    name, *permissions = input().split()
    files[name] = set(permissions)

m = int(input())
for i in range(m):
    action, name = input().split()
    if action == 'read' and 'R' in files[name]:
        out.append('OK')
    elif action == 'write' and 'W' in files[name]:
        out.append('OK')
    elif action == 'execute' and 'X' in files[name]:
        out.append('OK')
    else:
        out.append('Access denied')
for x in out:
    print(x)
