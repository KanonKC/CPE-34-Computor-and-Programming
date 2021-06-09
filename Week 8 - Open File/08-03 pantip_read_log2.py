with open(input('File name: '),'r') as f:
    data = {}
    # Topic
    h = f.readline().strip().split(',')
    for i in h:
        data[i] = []
    hK = [i for i in data] # Dict Key
    totalLine = 1
    # Number Data
    for i in f:
        totalLine += 1
        d = i.strip().split(',')
        for j in range(len(d)):
            try:
                data[hK[j]].append(int(d[j]))
            except:
                data[hK[j]].append(d[j])
    # print(data['uid'])

    # Sort by User
    du = data['uid']
    byus = {du[i]:[data[k][i] for k in data if k != 'uid'] for i in range(len(du))}
    # print(byus)

    # Data Sorting:
    # - Sort by User ===> byus (dict)
    # - Sort by Room ===> data (dict)

    sumData = {i:sum(data[i]) for i in data if i != 'uid'}
    sumUser = {i:sum(byus[i]) for i in byus}

# ====================================================================================================

def c1():
    print(totalLine)

def c2():
    top = 0
    topName = ""
    for i in sumData:
        if sumData[i] > top:
            top = sumData[i]
            topName = i
    print(topName)

def c3():
    bp = sorted(data['blueplanet'],reverse=True)
    print(bp[0],bp[1],bp[2])

def c4():
    top = 0
    topName = ""
    for i in sumUser:
        if sumUser[i] > top:
            top = sumUser[i]
            topName = i
    print(topName,top)

def c5():
    tv = data['tvshow'].index(max(data['tvshow']))
    print(data['uid'][tv],max(data['tvshow']))

def c6():
    ko = data['korea']
    c = 0
    for i in range(len(ko)):
        if ko[i] > 500:
            c += 1
    print(c)

def c7():
    siam = data['siam']
    food =  data['food']
    c = 0
    for i in range(len(siam)):
        if siam[i] > food[i]:
            c += 1
    print(c)

def c8():
    # for i user raj/all * 100
    inRaj = hK.index('rajdumnern') # Index Raj in User Dict
    perRaj = {i:byus[i][inRaj]/sumUser[i] for i in byus}
    
    # Find Most
    top = 0
    topName = ""
    for i in perRaj:
        if perRaj[i] > top:
            top = perRaj[i]
            topName = i
    print(topName)

def c9():
    sortUser = {i:sorted(byus[i],reverse=True) for i in byus}
    perFor2 = {i:(sortUser[i][0]+sortUser[i][1])/sumUser[i] for i in sortUser}
    # print(perFor2)

    # > 0.7
    c = 0
    for i in perFor2:
        if perFor2[i] > 0.7:
            c += 1
    print(c)

def c10():
    p = data['pantip']
    c = 0
    for i in range(len(p)):
        if p[i] == 0:
            c += 1
    print(c)

# ====================================================================================================

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