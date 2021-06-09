import json

# with open('worldpopulation.json','r') as f:
with open(input('File Name: '),'r') as f:
    data = json.load(f)
    # print(data)

def c1():
    nCountry = 0
    for i in data:
        nCountry += 1
    print(nCountry)

def c2():
    pop = 0
    for i in range(len(data)):
        pop += int(data[i]['population'])
    print(pop)

def c3():
    cLetter = 0
    moreThanFive = 0
    for i in range(len(data)):
        ac = data[i]['country']
        if ac[0] == "C":
            cLetter += 1
        if len(ac) > 5:
            moreThanFive += 1
    print(cLetter)
    print(moreThanFive)

def c4():
    gt500M = 0        # 1)มากกว่า 500 ล้านคน
    mid = 0           # 2)ระหว่าง 250 ถึง 750 ล้านคน
    lt10M = 0         # 3)น้อยกว่า 10 ล้าน
    for i in range(len(data)):
        p = int(data[i]['population'])
        if p > 500000000:
            gt500M += 1
        if p > 250000000 and p < 750000000:
            mid += 1
        if p < 10000000:
            lt10M += 1
    print(gt500M)
    print(mid)
    print(lt10M)

def c5():
    topPop = sorted([float(i['World']) for i in data],reverse=True)
    top20 = sum([topPop[i] for i in range(20)])*100
    top50to150 = sum([topPop[i] for i in range(49,150)])*100
    print(f'{top20:.2f}')
    print(f'{top50to150:.2f}')


# def c5():
#     topPop = sorted([int(i['population']) for i in data],reverse=True)
#     sumTop20 = sum([topPop[i] for i in range(20)])
#     sum50to150 = sum([topPop[i] for i in range(49,150)])
#     sumPop = sum(topPop)
#     print(f"{(sumTop20/sumPop)*100:.2f}")
#     print(f"{(sum50to150/sumPop)*100:.2f}")
#     # print(topPop[49]-topPop[149])

x = int(input('Input : '))
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