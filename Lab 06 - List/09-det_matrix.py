def detfor2(mat):
    return (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])

def minor(matA,i,j):
    mat = []
    for a in range(len(matA)):
        mat.append(matA[a].copy())
    del mat[i]
    for k in range(len(mat)):
        del mat[k][j]
    return detfor2(mat)

def cofactor(mat,i,j):
    return ((-1)**(i+j))*minor(mat,i,j)

def det(mat):
    return (mat[0][0]*cofactor(mat,0,0)) + (mat[0][1]*cofactor(mat,0,1)) + (mat[0][2]*cofactor(mat,0,2))

A = []
for i in range(3):
    Alist = []
    x = input(f"Row {i+1} : ")
    Alist = x.split(" ")
    for j in range(3):
        Alist[j] = int(Alist[j])
    A.append(Alist)

print(det(A))