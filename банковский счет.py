def deposit(name, sum):
    banks[name] = banks.get(name, 0) + int(sum)


def withdraw(name, sum):
    banks[name] = banks.get(name, 0) - int(sum)


def balance(name):
    if name not in banks:
        print('ERROR')
    else:
        print(banks[name])


def income(percent):
    for k, v in banks.items():
        if v > 0:
            banks[k] = int(v * ((int(percent) / 100) + 1))


banks = dict()
inFiles = open('input.txt')
for line in inFiles:
    line = line.split()
    if 'BALANCE' in line:
        balance(line[1])
    elif 'DEPOSIT' in line:
        deposit(line[1], line[2])
    elif 'WITHDRAW' in line:
        withdraw(line[1], line[2])
    elif 'INCOME' in line:
        income(line[1])
    else:
        withdraw(line[1], line[3])
        deposit(line[2], line[3])
inFiles.close()
