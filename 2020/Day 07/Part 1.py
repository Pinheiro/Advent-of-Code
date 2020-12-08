import re

I = [re.split(' bags contain | bag, | bags, ', x) for x in open("2020/Day 07/Input.txt").read().splitlines()]
for i in range(len(I)):
    for j in range(len(I[i])):
        I[i][j] = I[i][j].replace(' bags.', '')
        I[i][j] = I[i][j].replace(' bag.', '')
        if (I[i][j][0] in ['0','1','2','3','4','5','6','7','8','9']):
            I[i][j] = I[i][j][2:]

Q = ['shiny gold']

def getOuters(bag):
    for i in range(len(I)):
        for j in range(1, len(I[i])):
            if I[i][j] == bag:
                if I[i][0] not in Q:
                    Q.append(I[i][0])
                    break

q = 0
while q < len(Q):
    getOuters(Q[q])
    q += 1
print(len(Q) - 1)