import re
lst = [re.split('-| |: ', x) for x in open("Day02-1.in").read().splitlines()]
result = 0
for x in lst:
    if ((x[3].count(x[2]) >= int(x[0])) and ((x[3].count(x[2]) <= int(x[1])))):
        result += 1
print(result)