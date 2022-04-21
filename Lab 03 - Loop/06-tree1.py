hrec = h = int(input("h: "))
c = input("Character: ")
iv = input("Is the tree invert?(y/n): ")

logH = h//2

def leaf(space,char):
    for spc in range(0,space,1):
        print(" ",end="")
    for chr in range(0,char,1):
        print(c,end="")
    print()

# Invert Tree
if iv == "y":
    for i in range(1,logH + 1,1):
        leaf(h-1,1)

    for j in range(0,h,1):
        leaf(j,(h*2)-1)
        h -= 1

# Normal Tree
if iv == "n":
    for j in range(1,h+1,1):
        leaf(h-1,(j*2)-1)
        h -= 1
    for i in range(1,logH + 1,1):
        leaf(hrec-1,1)


