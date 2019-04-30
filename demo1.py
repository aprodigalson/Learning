from random import choice
import string
keyNum = 200
keyLength = 20
# wrapper ???
def printKey(func):
    def _printKey(length,num):
        for i in func(length,num):
            print(i)
    return _printKey

# get nums key
def getAllKey(length,num,result=None):
    if result is None:
        result = set()
    while len(result)<num:
        if getKey(length) in result:
            continue
        else:
            result.add(getKey(length))
    print(result)
    return result

# get one key
def getKey(length):
    baseChar = string.ascii_letters + string.digits
    keyList = [choice(baseChar) for _ in range(length)]
    return ''.join(keyList)

res = getAllKey(keyLength,keyNum)