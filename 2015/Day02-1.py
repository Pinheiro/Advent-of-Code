dimensionsStrings = [x.split('x') for x in open("2015/Day02.Input").read().splitlines()]
total = []
for dStr in dimensionsStrings:
    dInt = [int(x) for x in dStr]
    sides = []
    sides.append(dInt[0]*dInt[1])
    sides.append(dInt[0]*dInt[2])
    sides.append(dInt[1]*dInt[2])
    total.append(2*sum(sides) + min(sides))
print(sum(total))