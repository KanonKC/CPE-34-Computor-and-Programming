
# class Matrix:
#     def __init__(self,mat):
#         self.mat = mat
#         self.origin = mat

#     def __str__(self):
#         formatString = ""
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[i])):
#                 formatString += str(self.mat[i][j]) + "   "
#             formatString += '\n'
#         return formatString

#     def plus(self,mat2):
#         self.mat = [[self.mat[i][j] + mat2.mat[i][j] for j in range(len(mat2.mat[i]))] for i in range(len(self.mat))]

#     def transpost(self):
#         self


def readMatrixFile(file):
    with open(file,'r') as m:
        raw = [i.strip().split() for i in m.readlines()]
        data = [[float(raw[i][j]) for j in range(len(raw[i]))] for i in range(len(raw))]
        return data

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f"{round(mat[i][j],2):^6}",end=" ")
        print()

# O P E R A T O R

def matPlus(a,b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matMinus(a,b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def matMulCon(mat,c):
    return [[mat[i][j]*c for j in range(len(mat[i]))] for i in range(len(mat))]

def matMul(a,b):
    return [[sum([a[i][k]*b[k][j] for k in range(len(a[0]))]) for j in range(len(b[0]))] for i in range(len(a))]

def matPow(mat,c):
    res = [[mat[i][j] for j in range(len(mat[i]))] for i in range(len(mat))]
    for i in range(1,c):
        res = matMul(res,res)
    return res

A = readMatrixFile('A.txt')
B = readMatrixFile('B.txt')
C = readMatrixFile('C.txt')

no1 = matPlus(transpose(A),matMulCon(C,7))
no2 = matPow(B,3)
no3 = matMinus(transpose(matMul(A,B)),C)
no4 = matMul(C,matPlus(transpose(C),matMulCon(A,2)))

while True:
    exec(f"printMatrix(no{input('(Enter 1,2,3 or 4): ')})")