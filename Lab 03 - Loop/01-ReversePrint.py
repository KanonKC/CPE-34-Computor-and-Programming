n = []

while True:
     x = int(input(""))
     if x == 0:
         break
     n.append(x)

nRev = []

for i in range(1,len(n) + 1,1):
    nRev.append(n[-i])

for j in range(0,len(nRev),1):
    print(nRev[j],end=" ") 