import re
lst = [re.split('-| |: ', x) for x in open("2020/Day02.Input").read().splitlines()]
result = 0
for x in lst:
    if ((x[3].count(x[2]) >= int(x[0])) and ((x[3].count(x[2]) <= int(x[1])))):
        result += 1
print(result)