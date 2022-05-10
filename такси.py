n = sorted(list(map(int, input().split())))
tariff = sorted(list(map(int, input().split())), reverse=True)
summa = 0
for i in range(len(n)):
    summa += n[i] * tariff[i]
print(summa)
