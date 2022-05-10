names = list()
votes = list()
sumVotes = 0
inFile = open('input.txt', 'r')
for line in inFile:
    line = line.split()
    partyName = ' '.join(line[:-1])
    partyVotes = int(line[-1])
    names.append(partyName)
    votes.append(partyVotes)
    sumVotes += partyVotes
inFile.close()
mandate = list()
fraPart = []
sumMandates = 0
for i in range(len(names)):
    partyMandates = (votes[i] * 450) / sumVotes
    sumMandates += int(partyMandates)
    mandate.append(int(partyMandates))
    fraPart.append(partyMandates - int(partyMandates))
while sumMandates < 450:
    i = 0
    for j in range(1, len(fraPart)):
        if (
                (fraPart[j] > fraPart[i]) or
                (fraPart[j] == fraPart[i] and votes[j] > votes[i])
        ):
            i = j
    mandate[i] += 1
    sumMandates += 1
    fraPart[i] = 0
for k in range(len(names)):
    print(names[k], mandate[k])
