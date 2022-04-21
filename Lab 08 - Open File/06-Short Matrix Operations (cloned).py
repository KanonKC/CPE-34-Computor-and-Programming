# 1)
print([[0 for j in range(n)] for i in range(m)])

# 2)
print([[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))])

# 3)
print([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])

# 4)
print([[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))])