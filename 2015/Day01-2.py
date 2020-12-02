directions = [x for x in open("2015/Day01.Input").read()]
level = 0
item = 0
result = -1
for d in directions:
    item += 1
    if (d == '('):
        level += 1
    if (d == ')'):
        level -= 1
    if (level == -1):
        result = item
        break
print(result)