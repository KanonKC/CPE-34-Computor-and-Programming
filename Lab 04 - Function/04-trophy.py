def hash(space,item):
    for s in range(1,space+1):
        print(" ",end="")
    print("=",end="")
    for i in range(1,item+2):
        print("#",end="")
    print("=",end="")
    print()

def line(space,item):
    for s in range(1,space+1):
        print(" ",end="")
    print("=",end="")
    for i in range(1,item+2):
        print("=",end="")
    print("=",end="")
    print()

n = int(input("n: "))

space = 0

# TOP
for a in range(n*2,1,-2):
    line(space,a)
    hash(space,a)
    space += 1

for b in range(1,n+2,1):
    print(" ",end="")
print("=")
# BASE

h = n//2

for a in range(1,h*2,2):
    if a == (h*2)-1:
        hash(space,a-1)
    else:
        hash(space,a-1)
        line(space,a-1)
    space -= 1