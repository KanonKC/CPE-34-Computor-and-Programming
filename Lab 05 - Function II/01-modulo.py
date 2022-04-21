a = int(input("N: "))
m = int(input("M: "))

modeDict = {}

for i in range(1,a+1):
    n = int(input(f"Input number {i}: "))
    mod = n % m
    if modeDict.get(mod): # IF IN DICT
        modeDict[mod] += 1
    else:
        modeDict[mod] = 1

print(len(modeDict))