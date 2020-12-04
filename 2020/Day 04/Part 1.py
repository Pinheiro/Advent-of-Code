def isValid(s):
    result = False
    if (s.find('byr:') != -1):
        if (s.find('iyr:') != -1):
            if (s.find('eyr:') != -1):
                if (s.find('hgt:') != -1):
                    if (s.find('hcl:') != -1):
                        if (s.find('ecl:') != -1):
                            if (s.find('pid:') != -1):
                                result = True
    return result

inp = [x for x in open("2020/Day 04/Input.txt").readlines()]

i = 0
while True:
    try:
        if (inp[i + 1] != '\n'):
            inp[i] = inp[i] + ' ' + inp[i + 1]
            del inp[i + 1]
        else:
            del inp[i + 1]
            i += 1
    except:
        break

validCount = 0
for i in range(len(inp)):
    inp[i] = inp[i].strip('\n')
    inp[i] = inp[i].replace('\n', '')
    if isValid(inp[i]):
        validCount += 1
    #print(inp[i], validCount)

print(validCount)