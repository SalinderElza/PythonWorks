N = int(input())
ListLang = []
SetLangAll = set()
SetLangMin = set()
for j in range(N):
    M = int(input())
    for i in range(M):
        ListLang.append(input())
    if j == 0:
        SetLangMin = set(ListLang)
    SetLangAll |= set(ListLang)
    SetLangMin &= set(ListLang)
    ListLang = []
print(len(SetLangMin))
for i in SetLangMin:
    print(i)
print(len(SetLangAll))
for i in SetLangAll:
    print(i)
