counters = {}
strWord = ''
inFile = open('input.txt', 'r')
for line in inFile:
    strWord = strWord + ' ' + line.replace('\n', '')
inFile.close()
for word in strWord.split():
    counters[word] = counters.get(word, 0) + 1
    print(counters[word] - 1, end=' ')
