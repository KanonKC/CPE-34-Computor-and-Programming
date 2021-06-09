n = int(input())

for i in range((n-1)//2):
    if i == 0:
        for i in range(n):
            print(".",end="")
    else:
        print(".",end="")
        for j in range(i-1):
            print(" ",end="")
        print(".",end="")
        for k in range(n-4-(2*(i-1))):
            print(" ",end="")
        print(".",end="")
        for l in range(i-1):
            print(" ",end="")
        print(".",end="")
    print()

print(".",end="")
for j in range((n-3)//2):
    print(" ",end="")
print(".",end="")
for j in range((n-3)//2):
    print(" ",end="")
print(".",end="")
print()

for i in range(((n-1)//2)-1,-1,-1):
    if i == 0:
        for i in range(n):
            print(".",end="")
    else:
        print(".",end="")
        for j in range(i-1):
            print(" ",end="")
        print(".",end="")
        for k in range(n-4-(2*(i-1))):
            print(" ",end="")
        print(".",end="")
        for l in range(i-1):
            print(" ",end="")
        print(".",end="")
    print()