day = int(input("Day: "))

z = 0
i = 1
x = 1
y = 0
pre = 1

while i <= day:
    if i % 2 != 0: #Keep as Z as X
        x = x + y
        print(x,end=" ")
    else:
        y = x + y
        print(y,end=" ")
        if i == 1:
            y += 1
    i += 1
