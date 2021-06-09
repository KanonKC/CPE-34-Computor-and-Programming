def chartoint(num):
    for i in range(len(num)):
        num[i] = int(num[i])
    return num

def mintomax(num):
    for j in range(len(num)):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                reca = num[i]
                num[i] = num[i+1]
                num[i+1] = reca
    return num

def cut(num):
    temp = []
    for i in range(len(num)):
        if num[i] in temp:
            pass
        else:
            temp.append(num[i])
    return temp

num = input().split()

num = chartoint(num)

num = mintomax(num)

num = cut(num)

for i in range (0,len(num),1):
    print(num[i],end=' ')