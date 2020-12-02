lstNumbers = sorted([int(x) for x in open("Day01-1.in").readlines()])
maxIndex = len(lstNumbers)
for i in range(maxIndex - 2):
    for j in range(i + 1, maxIndex - 1):
        for k in range(j + 1, maxIndex):
           if (lstNumbers[i] + lstNumbers[j] + lstNumbers[k]) == 2020:
               print(lstNumbers[i] * lstNumbers[j] * lstNumbers[k])