def create(space,item):
    for s in range(1,space+1):
        print(" ",end="")
    for i in range(1,item+1):
        print("#",end="")
    print()

n = 21
h = (n//2)+1

# TOP
for i in range(h):
    create((n//2)-i,(i*2)+1)

# BOT
for j in range(0,h):
    create(j+1,n-(2*(j+1)))

# 2 1
# 1 3
# 0 5

# 1 3
# 2 1

