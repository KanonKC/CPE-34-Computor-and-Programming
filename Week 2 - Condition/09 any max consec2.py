modeKey = 0
modeVal = 0
recmodeKey = 0
recmodeVal = 0

while True:
    n = int(input(""))
    if n == 0:
        break
    if n == modeKey: # SAME
        modeVal += 1
    else: # NEW
        if modeVal > recmodeVal:
            recmodeKey = modeKey
            recmodeVal = modeVal
        modeKey = n
        modeVal = 1

print(recmodeVal)
print(recmodeKey)