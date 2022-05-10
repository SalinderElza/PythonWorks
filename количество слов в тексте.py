myList = open('input.txt', 'r', encoding='utf8')
counter = []
reading = myList.read().split('\n')
for i in reading:
    counter += i.split()
print(len(set(counter)))
