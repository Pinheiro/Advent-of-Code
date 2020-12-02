directions = [x for x in open("2015/Day01.Input").readlines()]
print(directions[0].count("(") - directions[0].count(")"))