lstNumbers = sorted([int(x) for x in open("Day01-1.in").readlines()])
for x in lstNumbers:
    if (2020 - x) in lstNumbers: print(x * (2020 - x))