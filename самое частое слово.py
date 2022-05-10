fin = open('input.txt', 'r')
d = {}
for line in fin:
    words = line.strip().split()
    for word in words:
        d[word] = d.get(word, 0) + 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])
