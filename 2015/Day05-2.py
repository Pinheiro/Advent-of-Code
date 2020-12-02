def containPair(s): # xyaaaaxy
    result = False
    for i in range(len(s)-1):
        if (s.count(s[i:i+2]) > 1):
            result = True
            break
    return result
    
def containRepeat(s): # xyx
    result = False
    for i in range(len(s)-2):
        if (s[i] == s[i+2]):
            result = True
            break
    return result

def isNice(s):
    return containPair(s) and containRepeat(s)

strings = [x for x in open("2015/Day05.Input").read().splitlines()]
niceList = [isNice(s) for s in strings]
print(niceList.count(True))