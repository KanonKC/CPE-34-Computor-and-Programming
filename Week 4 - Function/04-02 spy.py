a = input("")
allList = a.split(" ")
n = int(allList[0])
aList = allList[1:]


ascNonIntList = []

for i in range(0,len(aList),n+1):
        ascNonIntList.append(aList[i])

ascList = []
for i in range(len(ascNonIntList)):
    ascList.append(int(ascNonIntList[i]))

for j in range(len(ascList)):
    print(chr(ascList[j]),end="")