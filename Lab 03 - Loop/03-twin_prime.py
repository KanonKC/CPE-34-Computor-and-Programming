def isPrime(num):
    i = 2
    while i <= num:
        if num % i == 0 and i < num:
            i = num
            return False
        elif i == num:
            return True
        else:
            i += 1

n = int(input("N: "))

while not isPrime(n) or not isPrime(n+2):
    n += 1

print(f"({n}, {n+2})")
