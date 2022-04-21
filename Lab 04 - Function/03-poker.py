card = input("Cards: ")
cardList = card.split(" ")

isHigh = True
#print(cardList)

key = []
keyVal = [] # 1 1 1 2 3 ====> [ [1,3] , [2,1] , [3,1] ]

for i in range(len(cardList)):
    if cardList[i] in key:
        for j in range(len(keyVal)):
            if cardList[i] == keyVal[j][0]:
                keyVal[j][1] += 1
    else:
        keyVal.append([cardList[i],1])
        key.append(cardList[i])

for i in range(len(keyVal)):
    if keyVal[i][1] == 4:
        print('Mark got "Four of a kind"')
        isHigh = False
        break
    if keyVal[i][1] == 3:
        if keyVal[i+1][1] == 2 or keyVal[i-1][1] == 2:
            print('Mark got "Full House"')
            isHigh = False
            break
        else:
            print('Mark got "Three of a kind"')
            isHigh = False
            break
    if keyVal[i][1] == 2:
        if keyVal[i+1][1] == 3 or keyVal[i-1][1] == 3:
            print('Mark got "Full House"')
            isHigh = False
            break
        else:
            print('Mark got "Three of a kind"')
            isHigh = False
            break

if(isHigh):
    print('Mark got "High Card"')