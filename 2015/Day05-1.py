def isNice(s):
    vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    twice = False
    for i in range(len(s)-1):
        if (s[i] == s[i+1]):
            twice = True
            break
    forbidden = s.count('ab') + s.count('cd') + s.count('pq') + s.count('xy')
    return (vowels >= 3) and (twice) and (forbidden == 0)

strings = [x for x in open("2015/Day05.Input").read().splitlines()]
nice = 0
for s in strings:
    if isNice(s):
        nice += 1
print(nice)