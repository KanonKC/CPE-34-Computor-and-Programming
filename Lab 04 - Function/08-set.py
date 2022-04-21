a = input("Input setA: ")
b = input("Input setB: ")

aList = a.split(" ")
bList = b.split(" ")

setA = []
setB = []

for a in range(len(aList)):
    setA.append(int(aList[a]))

for b in range(len(bList)):
    setB.append(int(bList[b]))


minL = 0
maxL = 0

inter = []
# INTERSECT

if len(setA) >= len(setB):
    for i in range(len(setA)):
        if setA[i] in setB:
            inter.append(setA[i])
elif len(setA) < len(setB):
    for i in range(len(setB)):
        if setB[i] in setA:
            inter.append(setB[i])

inter.sort()
#print(inter)

setAmB = []
# A - B
for a in range(len(setA)):
    if setA[a] in inter:
        pass
    else:
        setAmB.append(setA[a])

setAmB.sort()
#print(setAmB)

setBmA = []
# B - A
for b in range(len(setB)):
    if setB[b] in inter:
        pass
    else:
        setBmA.append(setB[b])

setBmA.sort()
#print(setBmA)

union = []
# Union
for a in range(len(setA)):
    if setA[a] in union:
        pass
    else:
        union.append(setA[a])

for b in range(len(setB)):
    if setB[b] in union:
        pass
    else:
        union.append(setB[b])

union.sort()
#print(union)

print("A intersect B:",end=" ")
if len(inter) == 0:
    print("empty set",end="")
else:
    for i in inter:
        print(i,end=" ")
print()

print("A minus B:",end=" ")
if len(setAmB) == 0:
    print("empty set",end="")
else:
    for i in setAmB:
        print(i,end=" ")
print()

print("B minus A:",end=" ")
if len(setBmA) == 0:
    print("empty set",end="")
else:
    for i in setBmA:
        print(i,end=" ")
print()

print("A union B:",end=" ")
if len(union) == 0:
    print("empty set",end="")
else:
    for i in union:
        print(i,end=" ")
print()

