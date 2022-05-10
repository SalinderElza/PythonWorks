inFile = open('input.txt', 'r', encoding='utf8')
klass9, klass10, klass11 = [], [], []
for line in inFile.readlines():
    if int(line.split()[2]) == 9:
        klass9.append(int(line.split()[3]))
    elif int(line.split()[2]) == 10:
        klass10.append(int(line.split()[3]))
    else:
        klass11.append(int(line.split()[3]))
klass9.sort(key=int, reverse=True)
klass10.sort(key=int, reverse=True)
klass11.sort(key=int, reverse=True)
print(max(klass9[klass9.count(max(klass9)):]), end=' ')
print(max(klass10[klass10.count(max(klass10)):]), end=' ')
print(max(klass11[klass11.count(max(klass11)):]))
inFile.close()
