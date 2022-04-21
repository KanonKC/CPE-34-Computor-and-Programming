def matPlus(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matMinus(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matMulti(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

def printMat(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^6}",end=" ")
        print()

with open(input("File name: "),"r") as f:
    raw = [i.strip() for i in f if i.strip() != '']
    mat = {}
    emp = []
    opr = []
    c = 0
    for i in range(len(raw)):
        if raw[i] in ["+","-","*"]:
            opr.append(raw[i])
            mat[c] = emp
            emp = []
            c += 1
        else:
            emp.append([int(j) for j in raw[i].split()])
    mat[c] = emp
    emp = []
    c += 1
    # print(mat)

sumMat = mat[0]
match = 0
for i in range(len(opr)):
    if opr[i] == "+":
        sumMat = matPlus(sumMat,mat[i+1])
    elif opr[i] == "-":
        sumMat = matMinus(sumMat,mat[i+1])
    elif opr[i] == "*":
        sumMat = matMulti(sumMat,mat[i+1])
    #print(sumMat)
#print("Result")
printMat(sumMat)