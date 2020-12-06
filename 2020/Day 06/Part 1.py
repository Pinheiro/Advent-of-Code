inp = [x for x in open("2020/Day 06/Input.txt").read()]
g = [''] # list of groups where each item is a list of each person's answers
for i in range(len(inp)):
    c = inp[i]
    if c == '\n':
        if inp[i + 1] == '\n':
            g.append('')
    else:
        if (g[-1].find(inp[i]) == -1):
            g[-1] = g[-1] + inp[i]
print(sum(len(x) for x in g))