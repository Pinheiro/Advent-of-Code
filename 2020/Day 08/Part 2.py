I = [x.split(' ') for x in open("2020/Day 08/Input.txt").read().splitlines()]
M = list()
for i in range(len(I)):
    I[i].extend([False])
    if (I[i][0] == 'nop') or (I[i][0] == 'jmp'):
        M.append(i)
acc = 0
pI = 0
pM = -1
while True:
    I[pI][2] = True
    if I[pI][0] == 'acc':
        acc += int(I[pI][1])
        pI += 1
    elif I[pI][0] == 'jmp':
        pI += int(I[pI][1])
    elif I[pI][0] == 'nop':
        pI += 1
    if pI == len(I): # exit loop
        break
    if I[pI][2]: # infinit loop check
        if pM > -1: # undo last change
            if I[pM][0] == 'jmp':
                I[pM][0] = 'nop'
            elif I[pM][0] == 'nop':
                I[pM][0] = 'jmp'
        pM += 1
        # make next change
        if I[pM][0] == 'jmp':
            I[pM][0] = 'nop'
        elif I[pM][0] == 'nop':
            I[pM][0] = 'jmp'
        # restart
        acc = 0 # reset accumulator
        for i in range(len(I)):
            I[i][2] = False # reset infinit loop check
        pI = 0 # reset pointer
print(acc)