dimensionsStrings = [x.split('x') for x in open("2015/Day 02/Input.txt").read().splitlines()]
total = []
for dStr in dimensionsStrings:
    dInt = sorted([int(x) for x in dStr])
    total.append(2*(dInt[0]+dInt[1]) + dInt[0]*dInt[1]*dInt[2])
print(sum(total))