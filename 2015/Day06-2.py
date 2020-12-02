import re
instructions = [re.split(' |,', x) for x in open("2015/Day06.Input").read().splitlines()]
lights = [[0 for columns in range(1000)] for rows in range(1000)]

def processInstruction(i):
    x0 = int(i[1])
    y0 = int(i[2])
    x1 = int(i[3]) + 1
    y1 = int(i[4]) + 1
    if (i[0] == 'turnoff'):
        # turn off
        for x in range(x0, x1):
            for y in range(y0, y1):
                if (lights[x][y] > 0):
                    lights[x][y] -= 1
    elif (i[0] == 'turnon'):
        # turn on
        for x in range(x0, x1):
            for y in range(y0, y1):
                lights[x][y] += 1
    else:
        # toggle
        for x in range(x0, x1):
            for y in range(y0, y1):
                lights[x][y] += 2

for i in instructions:
    processInstruction(i)

print(sum([sum(row) for row in lights]))