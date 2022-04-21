w = float(input("w: ")) 
h = float(input("h: ")) 
a = float(input("a: ")) 
b = float(input("b: ")) 
c = float(input("c: "))

allArea = w * h

sidePool = (b+c)*a
midPool = (( (2*c) + (2*b) ) * a)/2

cementArea = allArea - (sidePool + midPool)

print("Area: %.2f" % cementArea)