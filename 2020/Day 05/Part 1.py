inp = [x for x in open("2020/Day 05/Input.txt").read().splitlines()]

def getID(boardingPass):
    row = 0
    rowMin = 0
    rowMax = 127
    col = 0
    colMin = 0
    colMax = 7
    for c in boardingPass:
        if (c == "F"):
            rowMax -= (rowMax + 1 - rowMin) / 2
            row = rowMax
        if (c == "B"):
            rowMin += (rowMax + 1 - rowMin) / 2
            row = rowMin
        if (c == "L"):
            colMax -= (colMax + 1 - colMin) / 2
            col = colMax
        if (c == "R"):
            colMin += (colMax + 1 - colMin) / 2
            col = colMin
    return int(row * 8 + col)

print(max([getID(x) for x in inp]))