disReq = int(input("Distance from starting point(m.): "))

dis = 0
Set = 0

if disReq == 0:
    print(0,end=" ")
else:
    while dis < disReq:
        dis += 5
        print(dis,end=" ")
        dis -= 2
        print(dis,end=" ")
        Set += 1

    while dis != disReq:
        dis -= 4
        print(dis,end=" ")
        dis += 3
        print(dis,end=" ")
        Set += 1

print()
print(f"Buzz moved {Set} set(s)")



