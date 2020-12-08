I = [x.split(' ') for x in open("2020/Day 08/Input.txt").read().splitlines()]
for i in range(len(I)):
    I[i].extend([False])
acc = 0
pI = 0
while True:
    I[pI][2] = True
    if I[pI][0] == 'acc':
        acc += int(I[pI][1])
        pI += 1
    elif I[pI][0] == 'jmp':
        pI += int(I[pI][1])
    else:
        pI += 1
    if I[pI][2]:
        break
print(acc)