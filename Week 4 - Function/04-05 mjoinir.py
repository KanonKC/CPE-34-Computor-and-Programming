def head(num):
    w = 9 + 3*(num-1)
    h = 5 + 2*(num-1)
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == (h-1)) and (j == 0 or j == (w-1)):
                print(" ",end="")
            else:
                print("o",end="")
        print()

def mid(num):
    h = 3 + (num-1)
    w = 1 + (num-1)
    s = 4 + (num-1)
    for i in range(h):
        for j in range(s):
            print(" ",end="")
        for k in range(w):
            print("o",end="")
        print()

def bot(num):
    h = 2 + (num-1)
    w = 3 + (num-1)
    for i in range(h):
        if i == (h-1):
            for j in range(w+1):
                print(" ",end="")
            for k in range(w-2):
                print("o",end="")
        else:
            for j in range(w):
                print(" ",end="")
            for k in range(w):
                print("o",end="")
        print()

gold = float(input("Input Gold: "))


g = int(gold // 1000)

if g < 1:
    print("Not enough gold.")
else:
    head(g)
    mid(g)
    bot(g)