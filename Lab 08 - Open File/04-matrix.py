# Matrix Function
def matPlus(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matMul(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

def printMat(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()

############################
filename = input('File name: ')

with open(filename,"r") as f:
    raw = [i.strip() for i in f]
    matDat = []
    mat = []
    for i in range(len(raw)):
        if raw[i] in ["+","*"]:
            matDat.append(mat)
            mat = []
        else:
            mat.append(raw[i])
    matDat.append(mat)
    matrix = {}
    for i in range(len(matDat)):
        matrix[i] = matDat[i]
    # Mapping 'n Casting
    for i in matrix:
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j].split()
    for i in matrix:
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                matrix[i][j][k] = int(matrix[i][j][k])
    # print(matrix)

printMat(matPlus(matMul(matrix[0],matrix[1]),matrix[2]))