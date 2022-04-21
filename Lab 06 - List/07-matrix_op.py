def transpose_matrix(A):
    # zMat = []
    # for i in range(len(A)):
    #     zList = []
    #     for j in range(len(A[i])):
    #         zList.append(A[i][j])
    #     zMat.append(zList)
    # #print(zMat)
    # # zMat as TempMat
    transMat = []
    for i in range(len(A[0])): #3
        transList = []
        for j in range(len(A)): #2
            transList.append(A[j][i])
        transMat.append(transList)
            #print(A,tempMat)
    return transMat

def plus_matrix(A,B):
    # RETURN AS MATRIX "A"
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] += B[i][j]
    return A

def minus_matrix(A,B):
    # RETURN AS MATRIX "A"
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] -= B[i][j]
    return A

def mul_matrix(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

def power_matrix(A,c):
    res = A
    for i in range(1,c):
        res = mul_matrix(res,A)
    return res

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

print_matrix(mul_matrix(plus_matrix(A,transpose_matrix(B)),minus_matrix(power_matrix(C,2),D)))