def calc(s):
    coc = len(s) # characters of code
    es1 = 0 # count escape sequence \\
    es2 = 0 # count escape sequence \"
    es3 = 0 # count escape sequence \x
    isEscape = False
    for c in s:
        if isEscape:
            if (c == '\\'):
                es1 += 1
                isEscape = False
            if (c == '"'):
                es2 += 1
                isEscape = False
            if (c == 'x'):
                es3 += 1
                isEscape = False
        else:
            if (c == '\\'):
                isEscape = True
    cim = coc - 2 - es1 - es2 - 3 * es3 # characters in memory
    return (coc - cim)  # calculated space

print(sum([calc(line) for line in open("2015/Day 08/Input.txt").read().splitlines()]))