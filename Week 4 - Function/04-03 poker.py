card = input("Cards: ")
cardList = card.split(" ")

isHigh = True

dictCard = {}

for i in range(len(cardList)):
    if dictCard.get(cardList[i]):
        dictCard[cardList[i]] += 1
    else:
        dictCard[cardList[i]] = 1

print(dictCard)

for j in dictCard:
    if dictCard[j] == 4:
        print('Mark got "Four of a kind"')
        isHigh = False
        break
    if dictCard[j] == 3 or dictCard[j] == 2:
        print("3 or 2")
        if dictCard[j] == 3:
            for k in dictCard:
                if dictCard[k] == 2:
                    print('Mark got "Full House"')
                    isHigh = False
                    break
            print('Mark got "Three of kind"')
            isHigh = False
            break
        elif dictCard[j] == 2:
            for k in dictCard:
                if dictCard[k] == 3:
                    print('Mark got "Full House"')
                    isHigh = False
                    break
            print('Mark got "Three of kind"')
            isHigh = False
            break
        break

if(isHigh):
    print('Mark got "High Card"')