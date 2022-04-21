def Fac(n):
    tFac = n
    if n == 0 or n == 1:
        return 1
    else:
        while n > 1:
            tFac *= n-1
            n -= 1
        return tFac

print(Fac(3) + 3)
print(Fac(1))
print(Fac(4))