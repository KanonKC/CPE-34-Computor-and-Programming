row = int(input("M: "))
col = int(input("N: "))

mat = [[int(j) for j in input().split()] for i in range(row)]

sortMat = [[0 for j in range(col)] for i in range(row)]

for i in range(col):
    diList = []
    for j in range(row):
        try:
            diList.append(mat[0+j][i+j])
        except:
            pass
    diList.sort()
    for j in range(row):
        try:
            sortMat[0+j][i+j] = diList[j]
        except:
            pass

for i in range(col):
    diList = []
    for j in range(row):
        try:
            diList.append(mat[i+j][0+j])
        except:
            pass
    diList.sort()
    for j in range(row):
        try:
            sortMat[i+j][0+j] = diList[j]
        except:
            pass


for i in range(len(sortMat)):
    for j in range(len(sortMat[0])):
        print(f"{sortMat[i][j]}",end=" ")
    print()