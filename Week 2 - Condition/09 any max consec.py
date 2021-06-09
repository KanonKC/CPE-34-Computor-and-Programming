modeN = 0
modeF = 0
nowN = 0
nowF = 0

while True:
    x = int(input(""))
    if x == 0:
        break
    if x != nowN:
        nowN = x
        nowF = 1
        if nowF > modeF:
            modeN = nowN
            modeF = nowF
    else:
        nowF += 1
        if nowF > modeF:
            modeN = nowN
            modeF = nowF

print(modeF)
print(modeN)