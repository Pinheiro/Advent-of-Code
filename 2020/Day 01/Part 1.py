lstNumbers = sorted([int(x) for x in open("2020/Day 01/Input.txt").readlines()])
for x in lstNumbers:
    if (2020 - x) in lstNumbers: print(x * (2020 - x))