def detfor2(mat):
    return (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])

def minor(matA,i,j):
    # mat =matA.copy()
    mat = []
    for a in range(len(matA)):
        mat.append(matA[a].copy())
    # print(mat)
    del mat[i]
    for k in range(len(mat)):
        del mat[k][j]
    # print(mat)
    # print(matA,mat)
    return detfor2(mat)

def cofactor(mat,i,j):
    #mat = matA.copy()
    return ((-1)**(i+j))*minor(mat,i,j)

def det(mat):
    return (mat[0][0]*cofactor(mat,0,0)) + (mat[0][1]*cofactor(mat,0,1)) + (mat[0][2]*cofactor(mat,0,2))

def matPlus(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

class Matrix:
    def __init__(self):
        print('input row of matrix A')
        self.a1 = [int(i) for i in '2 1 1'.split()] #'2 1 1'.split()] input('Row 1 : ').split()]
        self.a2 = [int(i) for i in '1 2 1'.split()] #'1 2 1'.split()] input('Row 2 : ').split()]
        self.a3 = [int(i) for i in '1 1 2'.split()] #'1 1 2'.split()] input('Row 3 : ').split()]
        self.matA = [self.a1,self.a2,self.a3]
        print('input row of matrix B')
        self.b1 = [int(i) for i in '2 1 1'.split()] #'2 1 1'.split()] input('Row 1 : ').split()]
        self.b2 = [int(i) for i in '1 2 1'.split()] #'1 2 1'.split()] input('Row 2 : ').split()]
        self.b3 = [int(i) for i in '1 1 2'.split()] #'1 1 2'.split()] input('Row 3 : ').split()]
        self.matB = [self.b1,self.b2,self.b3]

    def deter(self,mat):
        return det(self.mat)

        
mat = Matrix()

print(f'Det of Matrix(A) = {mat.deter(matA)}')
print(f'Det of Matrix(B) = {mat.deter(matB)}')