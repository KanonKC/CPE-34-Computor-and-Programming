bifGrid = [
        ["a","b","c","d","e"],
        ["f","g","h","ij","k"],
        ["l","m","n","o","p"],
        ["q","r","s","t","u"],
        ["v","w","x","y","z"]
]

def bifid(lett):
    for i in range(5):
        for j in range(5):
            if lett in bifGrid[i][j]:
                return [i+1,j+1]



text = "I’m Saito".lower()

codeGrid = [[],[]]
for i in range(len(text)):
    if text[i] in "qwertyuiopasdfghjklzxcvbnm":
        decp = bifid(text[i])
        codeGrid[0].append(decp[0])
        codeGrid[1].append(decp[1])

decodeGrid = []
for i in range(2):
    for j in range(len(codeGrid[0])):
        decodeGrid.append(codeGrid[i][j])
decodeGrid = [[decodeGrid[i],decodeGrid[i+1]] for i in range(0,len(decodeGrid),2)]
print(decodeGrid)
