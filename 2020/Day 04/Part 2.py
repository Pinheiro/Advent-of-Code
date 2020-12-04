import re

def getFieldValue(passport, field):
    f = passport.find(field) + 4
    if (f > 3):
        t = passport.find(' ', f)
        l = len(passport)
        if (t == -1):
            return passport[f:]
        else:
            return passport[f:t]
    else:
        return ''

def byrOk(passport):
    fieldValue = getFieldValue(passport, 'byr:')
    return (len(fieldValue) == 4) and (int(fieldValue) >= 1920) and (int(fieldValue) <= 2002)

def iyrOk(passport):
    fieldValue = getFieldValue(passport, 'iyr:')
    return (len(fieldValue) == 4) and (int(fieldValue) >= 2010) and (int(fieldValue) <= 2020)

def eyrOk(passport):
    fieldValue = getFieldValue(passport, 'eyr:')
    return (len(fieldValue) == 4) and (int(fieldValue) >= 2020) and (int(fieldValue) <= 2030)

def hgtOk(passport):
    fieldValue = getFieldValue(passport, 'hgt:')
    if (len(fieldValue) >= 4):
        value = int(fieldValue[:-2])
        units = fieldValue[-2:]
        cmOk = (units == 'cm') and (value >= 150) and (value <= 193)
        inOk = (units == 'in') and (value >= 59) and (value <= 76)
        return cmOk or inOk
    else:
        return False

def hclOk(passport):
    fieldValue = getFieldValue(passport, 'hcl:')
    if (len(fieldValue) == 7):
        if (fieldValue[0] == '#'):
            pattern = re.compile('[a-f0-9]+')
            return (pattern.fullmatch(fieldValue[1:]))
        else:
            return False
    else:
        return False

def eclOk(passport):
    fieldValue = getFieldValue(passport, 'ecl:')
    return (fieldValue == 'amb') or (fieldValue == 'blu') or (fieldValue == 'brn') or (fieldValue == 'gry') or (fieldValue == 'grn') or (fieldValue == 'hzl') or (fieldValue == 'oth')

def pidOk(passport):
    fieldValue = getFieldValue(passport, 'pid:')
    if (len(fieldValue) == 9):
        pattern = re.compile('[0-9]+')
        return (pattern.fullmatch(fieldValue))
    else:
        return False

def processPassport(passport):
    if byrOk(passport):
        if iyrOk(passport):
            if eyrOk(passport):
                if hgtOk(passport):
                    if hclOk(passport):
                        if eclOk(passport):
                            if pidOk(passport):
                                return True, 'valid'
                            else:
                                return False, 'invalid pid:'
                        else:
                            return False, 'invalid ecl:'
                    else:
                        return False, 'invalid hcl:'
                else:
                    return False, 'invalid hgt:'

            else:
                return False, 'invalid eyr:'
        else:
            return False, 'invalid iyr:'
    else:
        return False, 'invalid byr:'

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
    isValid, reason = processPassport(inp[i])
    if isValid:
        validCount += 1
    print(inp[i], reason)

print(validCount)