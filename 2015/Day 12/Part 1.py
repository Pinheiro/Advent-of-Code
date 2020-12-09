import re
print(sum(int(n) for n in re.findall(r'-?\d+', open("2015/Day 12/Input.txt").read())))