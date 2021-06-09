baseNum = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']

def reverse(li):
    rev = []
    for i in range(1,len(li)+1):
        rev.append(int(li[-i]))
    return rev

def anytoten(any,n): # num and base
    temp = any
    any = n
    n = temp
    nList = []
    for i in range(len(n)):
        nList.append(baseNum.index((n[i])))
    revN = reverse(nList)
    res = 0
    for j in range(len(revN)):
        res += revN[j] * (any**j)
    return int(res)

def tentoany(ten,m): # num and base
    mList = []
    while ten > 0:
        mList.append(ten%m)
        ten //= m
        #print(ten)
    revM = []
    for i in range(1,len(mList)+1):
        revM.append(mList[-i])
    newBase = ""
    for j in range(len(revM)):
        newBase = newBase + baseNum[revM[j]]
    return newBase

n = int(input(""))
m = int(input(""))
num = input("")

#print(anytoten(fromBase,n))

print(tentoany(anytoten(num,n),m))