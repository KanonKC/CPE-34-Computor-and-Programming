#n = input("").split()

#x = ['2','3','4']

def draw(m):
    for i in range(len(m)):
        for j in range(i+1):
            print(m[i],end="")
        print()

while True:
    n = input("").split()
    if n[0] == "0":
        print("Good Bye.")
        break
    else:
        draw(n)