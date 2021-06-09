# def top(num):
    # h = (n//2)+1
    # for i in range(h):
        # for s in range(h-1,-1,-1):
            # print(" ",end="")
        # for t in range(1,)    


n = 9
h = (n//2)+1

for t in range(h):
    for s in range(h-t-1):
        print(" ",end="")
    for i in range((t*2)+1):
        print("#",end="")
    print()
for b in range(h-1):
    for s in range(b+1):
        print(" ",end="")
    for i in range(n-(2*(b+1))):
        print("#",end="")
    print()
  #
 ###
#####