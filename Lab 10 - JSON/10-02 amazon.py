import json
with open(input('file name: ')) as f:
# with open('amazon1.json') as f:
    first = f.readlines()
    data = [json.loads(i) for i in first]

# Product Name : Product ID
nameId = {}
for i in range(len(data)):
    if data[i]['productID'] in nameId:
        pass
    else:
        nameId[data[i]['productID']] = data[i]['productName']

def c1(): # จำนวนรีวิวทั้งหมด
    print(len(data))

def c2(): # จำนวนผู้รีวิว
    userId = {}
    for i in range(len(data)):
        uid = data[i]['reviewerID']
        if uid in userId:
            userId[uid] += 1
        else:
            userId[uid] = 1
    return userId

def c3(): # จำนวนสินค้า
    proId = {}
    for i in range(len(data)):
        pid = data[i]['productID']
        if pid in proId:
            proId[pid] += 1
        else:
            proId[pid] = 1
    return proId

def c4():# จำนวนประเภทสินค้าหลัก
    mainCate = {}
    for i in range(len(data)):
        c = data[i]['category'].split('>')[0]
        if c in mainCate:
            mainCate[c] += 1
        else:
            mainCate[c] = 1
    print(len(mainCate))

def c5():# จำนวนประเภทสินค้าย่อยอันดับที่ 1
    cate1 = {}
    for i in range(len(data)):
        c = data[i]['category'].split('>')[1]
        if c in cate1:
            cate1[c] += 1
        else:
            cate1[c] = 1
    # print(cate1)
    print(len(cate1))

def c6():# ผู้รีวิวที่รีวิวสินค้ามากที่สุด
    userId = c2()
    top = 0
    topName = ""
    for i in userId:
        if userId[i] > top:
            top = userId[i]
            topName = i
    print(topName)

def c7(opr):# สินค้าที่ได้คะแนนเฉลี่ยสูงที่สุด (หากคะแนนเท่ากันให้เลือกสินค้าที่มีผู้รีวิวมากกว่า)
    proId = c3()
    star = {i:[] for i in proId} # productId : [1.0,2.0,3.0]
    for i in range(len(data)):
        p = data[i]['productID']
        r = data[i]['overall']
        star[p].append(r)
    # Find Average
    starBar = {}
    for i in star:
        starBar[i] = sum(star[i])/len(star[i])
    # print(starBar)
    
    # Find Top Rateing
    topStar = 0
    topPro = ""
    topRev = 0
    for i in starBar:
        if starBar[i] >= topStar and proId[i] > topRev:
            topStar = starBar[i]
            topRev = proId[i]
            topPro = i
    if opr == "post":
        print(nameId[topPro])
    elif opr == "get":
        return starBar,proId

def c8():# สินค้าที่มีคำเฉลี่ยต่อรีวิวทากที่สุด
    proId = c3()
    proPost = {i:[] for i in proId} # Key = Product ID | Value = Len Text
    for i in range(len(data)):
        r = len(data[i]['reviewText'].split())
        p = data[i]['productID']
        proPost[p].append(r)
    proPostBar = {i:sum(proPost[i])/len(proPost[i]) for i in proPost}
    topText = 0
    topPro = ""
    for i in proPostBar:
        if proPostBar[i] > topText:
            topText = proPostBar[i]
            topPro = i
    print(nameId[topPro])

# def c8():# สินค้าที่มีคำเฉลี่ยต่อรีวิวทากที่สุด
#     starBar,proId = c7("get")
#     starReview = {}
#     for i in starBar:
#         starReview[i] = starBar[i]/proId[i]
#     mostSR = 0
#     mostPro = ""
#     for i in starReview:
#         if starReview[i] > mostSR:
#             mostSR = starReview[i]
#             mostPro = i
#     print(nameId[mostPro])

x = int(input('input: '))
if x == 1:
    c1()
elif x == 2:
    print(len(c2()))
elif x == 3:
    print(len(c3()))
elif x == 4:
    c4()
elif x == 5:
    c5()
elif x == 6:
    c6()
elif x == 7:
    c7("post")
elif x == 8:
    c8()
