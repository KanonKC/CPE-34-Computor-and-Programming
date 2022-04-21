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

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
 

A = [
    [1,2],
    [3,4],
    [5,6]
    ]
#TempA = [
#   [1,2],
#   [3,4],
#   [5,6]
#]
#A = [
#   [1,2],
#   [3,4],
#   [5,6]
# ]

print_matrix(transpose_matrix(A))