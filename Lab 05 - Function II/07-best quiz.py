def findmax(a,n,m):
    nameList = []
    scoreList = []
    for i in range(n): # APPEND NAME LIST
        nameList.append(a[i][0])
    for i in range(n): # APPEND SCORE
        tempList = []
        for j in range(1,m+1):
            tempList.append(a[i][j])
        scoreList.append(tempList)
    # return scoreList,nameList
    # TRANSFROM STR TO INT
    for i in range(len(scoreList)):
        for j in range(len(scoreList[i])):
            scoreList[i][j] = int(scoreList[i][j])

    for i in range(len(scoreList)):
        scoreList[i].sort()
    for j in range(len(scoreList)):
        del scoreList[j][0]
    scoreSum = []
    for k in range(len(scoreList)):
        scoreSum.append(sum(scoreList[k]))
    return scoreSum,nameList
def printans(maxi,name):
    #maxScore = maxi.index(max(maxi))
    print(max(maxi))
    for i in range(len(name)):
        if maxi[i] == max(maxi):
            print(name[i])
n = int(input("n = "))

m = int(input("m = "))

a = []

for i in range (0,n,1):
    k = input().split()
    a.append(k)

maxi,name = findmax(a,n,m)

printans(maxi,name)

# printans(maxi,name)