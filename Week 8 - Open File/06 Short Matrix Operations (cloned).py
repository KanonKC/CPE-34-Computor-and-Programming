# def create_zero_matrix(m,n):
#      return [[0 for j in range(n)] for i in range(m)]

# print(create_zero_matrix(2,3))

# def plus(A,B):
#      return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# print(plus([[1,2],[3,4]],[[5,6],[7,8]]))

def transpose(A):
     return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3,4],[5,6]]))
print(transpose([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]]))