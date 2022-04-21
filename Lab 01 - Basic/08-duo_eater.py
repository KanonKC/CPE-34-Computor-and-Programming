s = int(input("Input starting food (S): "))
p = int(input("Input Paun's eating rate (P): "))
n = int(input("Input Gane's eating rate (n): "))

pTime = int(s / p)
rem1 = s % p

nTime = int(rem1 / n)
rem2 = rem1 % n

print("Paun eats",pTime,"time(s)")
print("Gane eats",nTime,"time(s)")
print("Remaining",rem2,"for dog")