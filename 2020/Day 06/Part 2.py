I = [x for x in open("2020/Day 06/Input.txt").read()]
G = [['']] # list of groups where each item is a list of each person's answers
for i in range(len(I)):
    c = I[i]
    if c == '\n':
        if I[i + 1] == '\n':
            G.append(['']) # new group
        if (i > 0) and (I[i - 1] != '\n') and (i < len(I) - 1) and (I[i + 1] != '\n'):
            G[-1].append('') # new person
    else:
        G[-1][-1] = G[-1][-1] + I[i]
r = 0
for g in G:
    for i in range(1, len(g)):
        for c in g[i]:
            if g[i - 1].find(c) == -1:
                g[i] = g[i].replace(c, '')
    r += len(g[-1])
print(r)