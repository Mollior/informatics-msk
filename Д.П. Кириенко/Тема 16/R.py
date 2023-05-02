clients = {}
out = []
def deposit(name, num):
    if name not in clients:
        clients[name] = 0
    clients[name] += num
def withdraw(name, num):
    if name not in clients:
        clients[name] = 0
    clients[name] -= num
def balance(name):
    if name not in clients:
        out.append('ERROR')
    else:
        out.append(clients[name])
def transfer(name1, name2, num):
    if name1 not in clients:
        clients[name1] = 0
    if name2 not in clients:
        clients[name2] = 0
    clients[name1] -= num
    clients[name2] += num
def income(p):
    for name in clients:
        if clients[name] > 0:
            income = clients[name] * p // 100
            clients[name] += income

while True:
    try:
        f = input().split()
        if f[0] == 'DEPOSIT':
            deposit(f[1],int(f[2]))
        elif f[0] == 'WITHDRAW':
            withdraw(f[1],int(f[2]))
        elif f[0] == 'BALANCE':
            balance(f[1])
        elif f[0] == 'TRANSFER':
            transfer(f[1],f[2],int(f[3]))
        elif f[0] == 'INCOME':
            income(int(f[1]))
    except:
        break
for x in out:
    print(x)
