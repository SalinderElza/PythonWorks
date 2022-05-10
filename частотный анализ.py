import sys


def makesort(lws):
    return -lws[0], lws[1]


letS = (str(sys.stdin.read()).split())
myLets = {}
for let in letS:
    myLets[let] = myLets.get(let, 0) + 1
myLets = [(fr, lt) for lt, fr in myLets.items()]
myLets.sort(key=makesort)
for i in range(len(myLets)):
    print(myLets[i][1])
