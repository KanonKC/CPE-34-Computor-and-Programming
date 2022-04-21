def mul_matrix(A,B):
    mulMat = []
    for i in range(len(A)): # 0 1 2
        rowList = []
        for j in range(len(A)): # 0 1 2
            proList = []
            for k in range(len(A)): # 0 1 2
                proList.append(A[i][k]*B[k][j])
            rowList.append(sum(proList))
        mulMat.append(rowList)
    return mulMat

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
        
def temp(A):
    tempMat = []
    for i in range(len(A)):
        tempMat.append(A[i])
    return tempMat

def power_matrix(A,c):
    res = A
    for i in range(1,c):
        res = mul_matrix(res,A)
    return res


A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2

print_matrix(power_matrix(A,c))