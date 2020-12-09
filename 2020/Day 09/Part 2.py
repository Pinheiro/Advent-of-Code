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
invN = I[i]
iBegin = 0
iEnd = 1
while True:
    s = sum(I[iBegin:iEnd + 1]) 
    if s == invN:
        smallest = min(I[iBegin:iEnd + 1])
        largest = max(I[iBegin:iEnd + 1])
        print(smallest + largest)
        break
    elif s < invN:
        iEnd += 1
    else:
        iBegin += 1
    if iBegin == iEnd:
        iEnd += 1