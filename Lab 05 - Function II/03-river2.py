def River(num):
    return num + sum([int(i) for i in str(num)])

def checkRiver(base,num,get=False):
    while base < num:
        base = River(base)
    if base == num:
        if get:
            return base
        return True
    return False

n = int(input())

base = {1:1,3:3,9:9}

isFound = False
while not isFound:
    for i in base:
        if checkRiver(base[i],n):
            isFound = True
            print(f"{i} {checkRiver(base[i],n,True)}")
            break
    n = River(n)