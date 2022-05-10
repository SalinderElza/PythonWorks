parties, votes, v = [], [], 1
with open("input.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        if line.strip() == "VOTES:":
            v = 0
        parties.append(line.strip()) if v else votes.append(line.strip())
res = [[i, votes.count(i)] for i in parties[1:]]
print(*[i[0] for i in sorted(res, key=lambda x: (-x[1], x[0]))], sep="\n")
