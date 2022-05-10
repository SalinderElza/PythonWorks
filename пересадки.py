a, b, c, d = [int(i) for i in input().split(' ')]
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
z = 0
for j in range(a, b + 1):
    for k in range(c, d + 1):
        if j == k:
            z += 1
print(z)
