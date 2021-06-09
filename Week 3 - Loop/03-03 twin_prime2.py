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
x = 0
prime1 = 0
prime2 = 0

while x < 2:
    if x == 0:
        if(isPrime(n)):
            # print("Yes")
            prime1 = n
            x += 1
            n += 2
        else:
            # print("No")
            n += 1
    elif x == 1:
        if(isPrime(n)):
            # print("Yes")
            prime2 = n
            x += 1
            n += 2
        else:
            # print("No")
            n -= 1
            x -= 1

print(f"({prime1}, {prime2})")




