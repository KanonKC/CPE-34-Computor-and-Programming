def mul_const(A,c):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

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
c = 2

print_matrix(mul_const(A,c))