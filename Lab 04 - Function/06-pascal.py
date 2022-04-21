def fac(n):
    res = 1
    for f in range(n,1,-1):
        res *= f
    return res

def com(n,r):
    return int(fac(n)/(fac(r)*fac(n-r)))

n = int(input("Input: "))

for i in range(n):
    for j in range(i+1):
        print(com(i,j),end=" ")
    print()



