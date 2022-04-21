def createList(con):
    nameList = {}
    #con = [i for i in f.read().strip().split('\n') if i != ""]
    for i in range(len(con)):
        for j in range(len(con[i])):
            if con[i][j] == " ":
                nameList[con[i][:j]] = [int(i) for i in con[i][j+1:].split()]
                break
    return nameList

def disMost(obj):
    for i in obj:
        obj[i].remove(max(obj[i]))
        obj[i].remove(min(obj[i]))
    return obj

def cal_score(obj):
    for name in obj:
        res = 0
        for s in obj[name]:
            res += s
            #print(res)
        obj[name] = res
    return obj

def printMax(obj):
    top = 0
    for name in obj:
        if obj[name] > top:
            top = obj[name]
    print(top)
    for name in obj:
        if obj[name] == top:
            print(name)

#####################################################
fileName = input("File name: ")
f = open(fileName,"r")
con = [i for i in f.read().strip().split('\n') if i != ""]

scoreB = cal_score(disMost(createList(con)))
printMax(scoreB)