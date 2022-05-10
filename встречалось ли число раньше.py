myList = list(map(int, input().split()))
before = set()
for elem in myList:
    if elem in before:
        print('YES')
    else:
        print('NO')
        before.add(elem)
