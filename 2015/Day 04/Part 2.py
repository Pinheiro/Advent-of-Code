import hashlib
key = 'ckczppom'
i = 0
while True:
    i += 1
    strhash = key + str(i)
    hexhash = hashlib.md5(strhash.encode()).hexdigest()
    if (hexhash[0:6] == '000000'):
        break
print(i)