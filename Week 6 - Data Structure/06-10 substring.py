def subCreate(text,sub):
    tList = text.split(sub)
    if len(tList) == 1:
        print("Not found")
    else:
        for i in range(len(tList)):
            if i == len(tList) - 1:
                print(tList[i],end="")
            else:
                print(tList[i],end="")
                print("[",end="")
                print(sub,end="")
                print("]",end="")

text = input("Text: ")
sub = input("Substring: ")

subCreate(text,sub)
#tList = text.split(sub)
#print(tList)

