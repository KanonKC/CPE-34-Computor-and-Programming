def isPrime(num):
    i = 2
    while i < num:
        if num%i==0:
            return False
        i += 1
    return True

def nextPrime(num):
    num += 1
    while True:
        if isPrime(num):
            return num
        else:
            num += 1

def factor(num):
    fact = []
    div = 2
    while num > 1:
        if num % div == 0:
            num //= div
            fact.append(div)
            div = 2
        else:
            div = nextPrime(div)
    return fact


a = factor(int(input('a : ')))
b = factor(int(input('b : ')))

# GCD
gcd = 1
lcm = 1
for i in range(len(a)):
    if a[i] in b:
        gcd *= a[i]
        b.remove(a[i])
    lcm *= a[i] # LCM

# LCM
for i in range(len(b)):
    lcm *= b[i]

print(f'GCD : {gcd}')
print(f'LCM : {lcm}')