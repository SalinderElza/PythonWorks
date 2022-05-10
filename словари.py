counter = int(input())
myDict = {}
for word in range(counter):
    first, second = input().split()
    myDict[first] = second
    myDict[second] = first
print(myDict[input()])
