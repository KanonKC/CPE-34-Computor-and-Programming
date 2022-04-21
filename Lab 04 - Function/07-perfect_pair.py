n = input("Input: ")
nList = n.split(" ")

num = []

sumN = []

for n in range(len(nList)):
    num.append(int(nList[n]))

for i in range(len(num)):
    for j in range(i+1,len(num)): # [1,2,3,4,5]
        sumN.append(num[i]+num[j])

sumList = []

for k in range(len(sumN)):
    if sumN[k] >= 0 and sumN[k] <= 100:
        sumList.append(sumN[k])
    elif sumN[k] < 0 and sumN[k] >= -100:
        sumList.append(sumN[k])

sumList.sort()

newSum = []

for i in range(len(sumList)):
    if sumList[i] in newSum:
        pass
    else:
        newSum.append(sumList[i])


for i in range(len(newSum)):
    print(newSum[i],end=" ")