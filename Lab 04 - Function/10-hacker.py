pas = input("")
isPass = True

i = 0
while i <= 2:
    x = input("")
    if x == pas[i]:
        i+=1
    else:
        print("Fail!!")
        isPass = False
        break

if (isPass):
    print("Succeed!!")
        