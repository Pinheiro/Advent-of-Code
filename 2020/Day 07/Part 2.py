import re

I = [re.split(' bags contain | bag, | bags, ', x) for x in open("2020/Day 07/Input.txt").read().splitlines()]
for i in range(len(I)):
    I[i][0] = [1, I[i][0]]
    for j in range(1, len(I[i])):
        I[i][j] = I[i][j].replace(' bags.', '')
        I[i][j] = I[i][j].replace(' bag.', '')
        if (I[i][j][0] in ['0','1','2','3','4','5','6','7','8','9']):
            I[i][j] = [int(I[i][j][0]), I[i][j][2:]]
        if I[i][j] == 'no other':
            I[i][j] = [0, I[i][j]]

def countBags(bag):
    counter = 0
    for i in range(len(I)):
        if I[i][0][1] == bag:
            counter += I[i][0][0]
            for j in range(1, len(I[i])):
                counter += I[i][j][0] * countBags(I[i][j][1])
    return counter

print(countBags('shiny gold') - 1)