directions = [x for x in open("2015/Day 01/Input.txt").readlines()]
print(directions[0].count("(") - directions[0].count(")"))