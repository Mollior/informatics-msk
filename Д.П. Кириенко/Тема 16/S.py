n = int(input())
eng_to_lat = {} 
for i in range(n):
    eng, *lat = input().split(' - ')
    lat = sorted(lat[0].split(', '))
    for l in lat:
        if l not in eng_to_lat:
            eng_to_lat[l] = set()
        eng_to_lat[l].add(eng)

print(len(eng_to_lat))
for l in sorted(eng_to_lat):
    print(l, '-', ', '.join(sorted(eng_to_lat[l])))
