n = int(input("N: "))



k = 0
i = 2
j = 2
while True:
    if k == 0:
        while i < n:
            if n % i == 0: # NOT PRIME NUMBER
                n += 1
            elif i == n - 1 and n % i != 0:
                k = 1
            i += 1

    elif k == 1:
        m = n + 2
        while j < m:
            if m % j == 0:
                k = 0
                n += 1
            elif i == m - 1 and m % i != 0:
                break
            j += 1

print(n)
print(m)

        