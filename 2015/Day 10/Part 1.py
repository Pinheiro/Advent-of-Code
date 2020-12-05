def LookAndSay(sequence):
    result = ''
    parts = list()
    i = 0
    digit = ''
    while (i < len(sequence)):
        if (digit.find(sequence[i]) == -1):
            digit = sequence[i]
            parts.append(digit)
        else:
            parts[-1] = parts[-1] + digit
        i += 1
    for p in parts:
        result = result + str(len(p)) + p[0]
    return result

#s = '1'
#s = '11'
#s = '21'
#s = '1211'
#s = '111221'
s = '1113222113'
print('0 ' + s + '\n')
for t in range(40):
    s = LookAndSay(s)
    #print(str(t + 1) + ' ' + s + '\n')
print(len(s))