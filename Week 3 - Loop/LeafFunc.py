n = int(input("N "))
m = int(input("M "))
c = input("C ")

def leaf(space,char):
    for x in range(0,space,1):
        print(" ",end="")
    for y in range(0,char,1):
        print(c,end="")
    print()

leaf(n,m)