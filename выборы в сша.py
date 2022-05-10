num_votes = {}
with open('input.txt') as in_file:
    for line in in_file:
        num_votes[line.split()[0]] = num_votes.get(line.split()[0], 0)\
                                     + int(line.split()[1])
    print(*[c + ' ' + str(num_votes[c]) for c in sorted(num_votes)], sep='\n')
