d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

i = 1
feb = 28

# Check Feb 28 29 days
if y % 4 == 0 and y % 100 != 0 and y % 400 != 0:
    feb = 29
else:
    feb = 28

while i < m + 1:
    if i in [2,4,6,8,9,11,13]:
        d += 31
    elif i in [5,7,10,12]:
        d += 30
    elif i == 3:
        d += feb
    i += 1

print(d)
