lands = {}
for land in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        lands[city] = country
for land in range(int(input())):
    print(lands[input()])
