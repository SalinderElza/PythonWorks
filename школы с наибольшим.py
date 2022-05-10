inFile = open('input.txt', 'r', encoding='utf8')
klass = {}
counter = 1
for line in inFile:
    school = int(line.split()[-2])
    if school in klass:
        klass[school] += 1
    else:
        klass[school] = counter
inFile.close()
spisok = []
for i in klass:
    if klass[i] == max(klass.values()):
        spisok.append(i)
print(*sorted(spisok))
