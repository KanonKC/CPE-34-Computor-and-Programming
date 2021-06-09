alp = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
num = ['1','2','3','4','5','6','7','8','9','0']

item = input("")
itemList = item.split(" ")

Alphabet = []
Number = []
Special = []

for i in range(len(itemList)):
    if itemList[i] in alp:
        Alphabet.append(itemList[i])
    elif itemList[i] in num:
        Number.append(itemList[i])
    else:
        Special.append(itemList[i])

print("Alphabet:",Alphabet)
print("Number:",Number)
print("Special:",Special)