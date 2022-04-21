nList = []
while True:
    n = str(input("Input: "))
    if int(n) == 0:
        break
    else:
        nList.append(n)

def isSpe(num):
    res = 0
    for i in range(len(num)):
        numI = int(num[i])
        res += int(numI)**(i+1)
    if res == int(num):
        print("Y",end="")
    else:
        print("N",end="")

for i in range(len(nList)):
    isSpe(nList[i])