print(sum([2 + s.count('\\') + s.count('"') for s in open("2015/Day 08/Input.txt").readlines()]))