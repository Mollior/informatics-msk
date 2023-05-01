votes = {}

f = open('input.txt','r')
for line in f:
    cand, count = line.split()
    if cand in votes:
        votes[cand] += int(count)
    else:
        votes[cand] = int(count)
for cand in sorted(votes.keys()):
    print(cand, votes[cand])
