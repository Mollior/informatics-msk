n = int(input())
cities_by_country = {} 

for i in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    cities_by_country.update({city: country for city in cities})

m = int(input())
count = []
for i in range(m):
    country = cities_by_country.get(input())
    count.append(country)
for x in count:
    print(x)
