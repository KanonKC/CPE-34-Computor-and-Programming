class Land:
    def __init__(self,field):
        self.field = field
        self.sold = [[False for j in range(len(self.field[0]))] for i in range(len(self.field))]

    def __str__(self):
        formatString = ''
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                formatString += str(self.field[i][j]) + ' '
            formatString += '\n'
        return formatString

    def __len__(self):
        return len(self.field)

    def dupField(self):
        return [[self.field[i][j] for j in range(len(self.field[0]))] for i in range(len(self.field))]

    def buy(self,r,c):
        self.sold[r][c] = True
        # UP
        if r-1 >= 0 and c >= 0 and r-1 < len(self.field) and c < len(self.field[0]):
            self.field[r-1][c] *= 1.1
        # RIGHT
        if r >= 0 and c+1 >= 0 and r < len(self.field) and c+1 < len(self.field[0]):
            self.field[r][c+1] *= 1.1
        # DOWN
        if r+1 >= 0 and c >= 0 and r+1 < len(self.field) and c < len(self.field[0]):
            self.field[r+1][c] *= 1.1
        # LEFT
        if r >= 0 and c-1 >= 0 and r < len(self.field) and c-1 < len(self.field[0]):
            self.field[r][c-1] *= 1.1
        return self.field[r][c]

    def moonBuy(self,i,j,clock):
        res = 0
        if clock == "cw":
            res += self.buy(i,j)
            res += self.buy(i,j+1)
            res += self.buy(i+1,j+1)
            res += self.buy(i+1,j)
        elif clock == "cc":
            res += self.buy(i+1,j)
            res += self.buy(i+1,j+1)
            res += self.buy(i,j+1)
            res += self.buy(i,j)
        return res

# ========================================================================================

landDesign = []
while True:
    subLand = [int(i) for i in input().split()]
    if subLand == []:
        break
    landDesign.append(subLand)

land = Land(landDesign)
possiblePrice = []

# res = land.moonBuy(0,0)
# print(land)
# print(res)

try:
    for i in range(len(land.field)-1):
        for j in range(len(land.field[0])-1):
            testLand = Land(land.dupField())
            res = testLand.moonBuy(i,j,'cw')
            possiblePrice.append(res)

    for i in range(len(land.field)-1):
        for j in range(len(land.field[0])-1):
            testLand = Land(land.dupField())
            res = testLand.moonBuy(i,j,'cc')
            possiblePrice.append(res)

    print(f'{min(possiblePrice):.2f}')
except:
    print("Can't Buy")
