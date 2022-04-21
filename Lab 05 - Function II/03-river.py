def river(num):
    res = num
    while num > 0:
        res += num%10
        num //= 10
    return res

def checkRiv(base,num):
    if base == num:
        return True
    while base <= num:
        if base == num:
            return True
        base = river(base)
    return False

n = int(input("N: "))
while True:
    if checkRiv(1,n):
        print("1",n)
        break
    if checkRiv(3,n):
        print("3",n)
        break
    if checkRiv(9,n):
        print("9",n)
        break
    n = river(n)
