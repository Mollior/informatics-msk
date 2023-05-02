n = int(input())

state_votes = {}
for i in range(n):
    state, num_electors = input().split()
    num_electors = int(num_electors)
    state_votes[state] = {"num_electors": num_electors}

for line in map(str.split, map(str.strip, sys.stdin)):
    state, candidate = line[:2]
    state_votes[state][candidate] = state_votes[state].get(candidate, 0) + 1

total_votes = {}
for state, votes in state_votes.items():
    for candidate, num_votes in votes.items():
        if candidate == "num_electors":
            continue
        total_votes[candidate] = total_votes.get(candidate, 0) + num_votes * votes["num_electors"]

for candidate, num_votes in sorted(total_votes.items(), key=lambda x: (-x[1], x[0])):
    print(candidate, num_votes)
