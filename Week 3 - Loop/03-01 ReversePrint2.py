nList = []
nRev = []

while True:
    n = int(input(""))
    if n == 0:
        break
    else:
        nList.append(n)

for i in range(len(nList)):
    nRev.append(nList[-i-1])

for p in range(len(nRev)):
    print(nRev[p],end=" ")
    