import json

with open(input('File name: '),'r') as f:
# with open('twitter.json','r') as f:
    data = json.load(f)

# DATA COLLECTOR ============================================================================================================================

authorPost = {} # Key = Author | Value = Post Time
for i in range(len(data)):
    a = data[i]['author']
    if a in authorPost:
        authorPost[a] += 1
    else:
        authorPost[a] = 1

topicPost = {} # Key = Topic Name | Value = Post Time
for i in range(len(data)):
    t = data[i]['topic']
    if t in topicPost:
        topicPost[t] += 1
    else:
        topicPost[t] = 1

priorPost = {} # Key = Priority Post | Value = Post Time
for i in range(len(data)):
    p = data[i]['topic_priority']
    if p in priorPost:
        priorPost[p] += 1
    else:
        priorPost[p] = 1

filterPost = {} # Key = Filtering Post | Value = Post Time
for i in range(len(data)):
    f = data[i]['filtering']
    if f in filterPost:
        filterPost[f] += 1
    else:
        filterPost[f] = 1

langPost = {} # Key = Language | Value = Post Time
for i in range(len(data)):
    l = data[i]['language']
    if l in langPost:
        langPost[l] += 1
    else:
        langPost[l] = 1

# FUNCTION ==================================================================================================================================

# > มีจำนวน tweet ทั้งหมดเท่าไหร่
def c1():
    print(len(data))

# > มีจำนวน tweet ทั้งหมดกี่คน
def c2():
    print(len(authorPost))

# > ผู้ใช้คนไหนมีจำนวนทวีตมากที่สุด
def c3():
    most = 0
    twtid = []
    for i in authorPost:
        if authorPost[i] > most:
            most = authorPost[i]
            twtid = [i]
        elif authorPost[i] >= most:
            twtid.append(i)
    for i in twtid:
        print(i)

# > มี topic ทั้งหมดกี่ topic และ topic ละเท่าไหร่
def c4():
    print(len(topicPost))

# > tweet ที่มีลำดับความสำคัญสูงสุดมีกี่ tweet
def c5():
    print(priorPost['ALERT'])

# > tweet ที่ไม่เกี่ยวข้อมีกี่ tweet
def c6():
    print(priorPost['UNIMPORTANT'])
    # print(filterPost['UNRELATED'])

# > มี tweet ที่ไม่ใช่ภาษาอังกฤษไหม (True / False)
def c7():
    if len(data) == langPost['EN']:
        print("False")
    else:
        print("True")

# > tweet ที่มีความยาวมากที่สุด มีกี่คำ
def c8():
    longestText = 0
    for i in range(len(data)):
        word = len(data[i]['text'].split())
        if word > longestText:
            longestText = word
    print(longestText)

# USER INTERFACE ==========================================================================================================================

x = int(input('input: '))
# x = 3
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