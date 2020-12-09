from itertools import combinations
I = [int(x) for x in open("2020/Day 09/Input.txt").read().splitlines()]
pSize = 25
i = pSize + 1
while True:
    P = [x for x in I[(i - pSize - 1):i]]
    combP = combinations(P, 2)
    combPsums = [sum(c) for c in combP]
    if not (I[i] in combPsums):
        break
    else:
        i += 1
print(I[i])