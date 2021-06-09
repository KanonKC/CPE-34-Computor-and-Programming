d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: ")) #2563

y -= 543 # 2020
day = 0

if (y%4 == 0 and y%100 != 0) and y % 400 != 0:
    isLeap = True
else:
    isLeap = False

for i in range(m):
    if i == 0:
        pass
    elif i in [1,3,5,7,8,10,12]:
        day += 31
    elif i == 2:
        if isLeap:
            day += 29
        else:
            day += 28
    else:
        day += 30

day += d

print(day)