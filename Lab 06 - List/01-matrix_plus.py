def plus_matrix(A,B):
    # RETURN AS MATRIX "A"
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] += B[i][j]
    return A

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()


A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

B = [
    [22,13,23],
    [54,43,21],
    [23,78,71]
    ]

#aPlusb = 
print_matrix(plus_matrix(A,B))