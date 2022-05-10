myList1 = set(input().split())
myList2 = set(input().split())
print(*sorted(myList1 & myList2, key=int))
