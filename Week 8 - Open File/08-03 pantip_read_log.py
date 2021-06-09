# filename = input('File name: ')

# with open(filename,'r') as f:
with open('pantip_read_20181015_20181222.csv','r') as f:
    name = f.readline().strip().split(",")
    # Sort by Web
    view = {k:[] for k in name} 
    line = 1
    for l in f:
        data = l.strip().split(',')
        line += 1
        for i in range(len(name)):
            try:
                view[name[i]].append(int(data[i]))
            except:
                view[name[i]].append(data[i])
    # Sort by User Viewer
    user = {view["uid"][k]:[view[i][k] for i in view if i != "uid"] for k in range(len(view["uid"])) }
    userSum = {}
    for i in user:
        userSum[i] = sum(user[i])

def c1():
    print(line)

def c2():
    top = 0
    topName = ""
    for i in view:
        try:
            if sum(view[i]) > top:
                top = sum(view[i])
                topName = i
        except:
            pass
    print(topName)

def c3():
    blueP = view["blueplanet"]
    #print(sorted(blueP,reverse=True))
    for i in range(3):
        print((sorted(blueP,reverse=True))[i],end=" ")
    print()

def c4():
    top = 0
    topName = ""
    for i in userSum:
        if userSum[i] > top:
            top = userSum[i]
            topName = i
    print(topName,top)

def c5():
    mostTv = max(view["tvshow"])
    ind = 0
    for i in view["tvshow"]:
        if i == mostTv:
            #print(ind)
            break
        ind += 1
    print(view['uid'][ind],mostTv)

def c6():
    over = 500
    count = 0
    for i in range(len(view['korea'])):
        if view['korea'][i] > 500:
            count += 1
    print(count)

def c7():
    siam = view['siam']
    food = view['food']
    count = 0
    for i in range(len(siam)):
        if siam[i] > food[i]:
            count += 1
    print(count)

def c8():
    # rajView / sumView * 100
    userSumKey = [i for i in userSum]
    perRaj = [(view['rajdumnern'][i]/userSum[userSumKey[i]])*100 for i in range(len(view['rajdumnern']))]
    top = 0
    indTop = 0
    for i in range(len(perRaj)):
        if perRaj[i] > top:
            top = perRaj[i]
            indTop = i
    print(view['uid'][indTop])

def c9():
    revSort = {i:sorted(user[i],reverse=True) for i in user}
    print(revSort)
    perID = {i:((revSort[i][0]+revSort[i][1])/sum(revSort[i]))*100 for i in revSort}
    print(perID)
    # print(revSort['pf4unt4gz1T3NV1j7f7y'])
    count = 0
    for i in perID:
        if perID[i] > 70:
            count += 1
    print(count)

def c10():
    count = 0
    for i in range(len(view['pantip'])):
        if view['pantip'][i] == 0:
            count += 1
    print(count)

def allCommand():
    try:
        x = int(input('enter number: '))
        if x == 1:
            c1()
        elif x == 2:
            c2()
        elif x == 3:
            c3()
        elif x == 4:
            c4()
        elif x == 5:
            c5()
        elif x == 6:
            c6()
        elif x == 7:
            c7()
        elif x == 8:
            c8()
        elif x == 9:
            c9()
        elif x == 10:
            c10()
        else:
            pass
    except ValueError:
        pass

allCommand()
# c9()
