m = list(map(int, input().split()))
day, n = [], []
lab = set()
for i in range(m[1]):
    n = list(map(int, input().split()))
    n = set(range(n[0], m[0] + 1, n[1]))
    lab = lab | n
flag = 0
for i in range(1, m[0] + 1):
    flag = flag + 1
    if flag == 6 or flag == 7:
        day.append(i)
        if flag == 7:
            flag = 0
print(len(lab - set(day)))
