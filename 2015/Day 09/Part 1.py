import re
from itertools import permutations

# distances between every pair of locations
D = [re.split(' to | = ', x) for x in open("2015/Day 09/Input.txt").read().splitlines()]

# locations to visit
L = set()
for d in D:
    L.add(d[0])
    L.add(d[1])

# route distance
S = list()

# possible routes
R = list(permutations(L))

# calculate each route distance

def distance(source, destination):
    for d in D:
        if ((d[0].find(source) != -1) and (d[1].find(destination) != -1)) or ((d[0].find(destination) != -1) and (d[1].find(source) != -1)):
            return int(d[2])

for r in R:
    S.append(0)
    for i in range(len(r) - 1):
        S[-1] += distance(r[i], r[i + 1])

print(str(min(S)))