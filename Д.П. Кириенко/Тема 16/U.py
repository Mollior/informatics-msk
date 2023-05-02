sales = {}
f = open('input.txt', 'r')
for x in f:
    b, i, q = x.split()
    q = int(q)
    if b in sales:
        if i in sales[b]:
            sales[b][i] += q
        else:
            sales[b][i] = q
    else:
        sales[b] = {i:q}
for b in sorted(sales):
    print(b + ':')
    for i in sorted(sales[b]):
        print(f'{i} {str(sales[b][i])}')
    
