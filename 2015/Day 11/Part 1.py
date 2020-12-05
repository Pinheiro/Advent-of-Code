length = 8
numIter = 10

# password must include one increasing straight of at least three letters
def c1(psw):
    r = False
    for i in range(length - 2):
        if ((ord(psw[i]) + 1) == ord(psw[i + 1])) and ((ord(psw[i + 1]) + 1) == ord(psw[i + 2])):
            r = True
    return r

# password must not contain the letters i, o, or l
def c2(psw):
    r = True
    for i in psw:
        if (i == 'i') or (i == 'o') or (i == 'l'):
            r = False
    return r

# password must not contain at least two different, non-overlapping pairs of letters
def c3(psw):
    firstPair = False
    firstLetter = ''
    secondPair = False
    for i in range(length - 1):
        if firstPair and (firstLetter != psw[i]) and (psw[i] == psw[i + 1]):
            secondPair = True
            break
        if (psw[i] == psw[i + 1]):
            firstPair = True
            firstLetter = psw[i]
    return secondPair

def isValid(psw):
    return c1(psw) and c2(psw) and c3(psw)

def incrPassword(psw):
    r = psw
    i = length - 1
    while (r[i] == 'z'):
        i -= 1
    if (i > -1):
        if (i == length - 1):
            r = r[:i] + chr(ord(r[i]) + 1)
        else:
            r = r[:i] + chr(ord(r[i]) + 1) + ('a' * (length - i - 1))
    return r

def nextPassword(psw):
    r = incrPassword(psw)
    while not isValid(r):
        r = incrPassword(r)
    return r

print(nextPassword('cqjxjnds'))