def wordOrder(text):
    order = []
    sortText = [i for i in sorted(text)]
    for i in range(len(text)):
        order.append(sortText.index(text[i]))
    return order
# ====================================================
text = input("Text: ").lower()
keyword = input("Keyword: ").lower()
# ====================================================
pos = 0
codeGrid = [[] for i in range(len(keyword))]
for i in range(len(text)):
    if text[i] in "qwertyuiopasdfghjklzxcvbnm":
        codeGrid[pos].append(text[i])
        if pos == len(keyword)-1:
            pos = 0
        else:
            pos += 1
# ====================================================
for i in range(len(codeGrid)):
    while len(codeGrid[i]) < len(codeGrid[0]):
        codeGrid[i].append("x")
# ====================================================
codeOrder = wordOrder(keyword)
codeGrid2 = {codeOrder[i]:codeGrid[i] for i in range(len(keyword))}
formatString = ""
for i in range(len(keyword)):
    for j in codeGrid2:
        if j == i:
            for k in codeGrid2[j]:
                formatString += k
            break
print(f'"{formatString}"')