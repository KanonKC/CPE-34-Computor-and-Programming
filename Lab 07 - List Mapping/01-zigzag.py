sen = input("Input sentence: ")
row = int(input("Input row: "))
isRev = False

z = [[] for i in range(row)]

r = 0
for i in range(len(sen)):
    z[r].append(sen[i])
    if (r == row-1 or r == 0) and i != 0:
        isRev = not isRev
    if isRev:
        r -= 1
    else:
        r += 1

for j in range(len(z)):
    for k in range(len(z[j])):
        print(z[j][k],end="")