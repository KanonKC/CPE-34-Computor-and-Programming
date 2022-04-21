a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))
e = int(input("Input e: "))

xi = [a,b,c,d,e]
exix = 0


ex = a + b + c + d + e
xBar = ex / 5

for i in range(0,5):
    exix += (xi[i] - xBar)**2

sd = (exix/5)**(1/2)

print("mean: %.3f" % xBar)
print("sd: %.3f" % sd)



