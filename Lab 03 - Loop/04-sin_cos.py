deg = float(input("degree: "))

rad = (deg * 3.14)/180

def Fac(n):
    tFac = n
    if n == 0 or n == 1:
        return 1
    else:
        while n > 1:
            tFac *= n-1
            n -= 1
        return tFac

# COSINE (cos)
sumCos = 0

for n in range(0,11,1):
    sumCos += (((-1)**n)*(rad**(2*n))) / Fac(2*n)


# SINE (sin)
sumSin = 0

for m in range(1,11,1):
    sumSin += (((-1)**(m-1))*(rad**((2*m)-1))) / Fac((2*m)-1)


print("sin(%.2f): %.10f" % (deg,sumSin))
print("cos(%.2f): %.10f" % (deg,sumCos))