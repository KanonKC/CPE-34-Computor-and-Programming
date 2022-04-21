pos = 0
numList = []

while pos < 5:
    n = int(input("Enter a positive number: "))
    if n > 0:
        numList.append(n)
        pos += 1
        
numList.sort()
print("sum:",sum(numList))
print("min:",numList[0])
print("max:",numList[4])
print("med:",numList[2])