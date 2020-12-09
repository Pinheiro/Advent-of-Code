import json

def sumNoRed(obj):
    if type(obj) == type(dict()):
        if "red" in obj.values():
            return 0
        return sum(map(sumNoRed, obj.values()))
    if type(obj) == type(list()):
        return sum(map(sumNoRed, obj))
    if type(obj) == type(0):
        return obj
    return 0

oJ = json.loads(open("2015/Day 12/Input.txt", 'r').read())
print(oJ.values())
print(sumNoRed(oJ))