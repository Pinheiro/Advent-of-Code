import re
lst = [re.split('-| |: ', x) for x in open("2020/Day02.Input").read().splitlines()]
result = 0
for x in lst:
    if ((x[3][int(x[0])-1] == x[2]) != (x[3][int(x[1])-1] == x[2])):
        result += 1
print(result)