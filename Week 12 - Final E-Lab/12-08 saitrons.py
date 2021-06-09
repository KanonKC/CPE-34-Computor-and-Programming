class Saitron:
    def __init__(self,field):
        self.hit = 0
        self.field = field
    
    def __str__(self):
        formatString = ""
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                formatString += self.field[i][j] + ' '
            formatString += '\n'
        return formatString
    
    def reflect(self,i,j,direct):
        if self.field[i][j] == 'O':
            return direct
        elif self.field[i][j] == "\\": # \
            self.hit += 1
            if direct == 'w':
                return 'a'
            elif direct == 'a':
                return 'w'
            elif direct == 's':
                return 'd'
            elif direct == 'd':
                return 's'
        elif self.field[i][j] == "/": # /
            self.hit += 1
            if direct == 'w':
                return 'd'
            elif direct == 'a':
                return 's'
            elif direct == 's':
                return 'a'
            elif direct == 'd':
                return 'w'
        
    def move(self,i,j,key):
        if key == 'w':
            # self.field[i][j] = 'S'
            return i-1,j
        elif key == 'a':
            # self.field[i][j] = 'S'
            return i,j-1        
        elif key == 's':
            # self.field[i][j] = 'S'
            return i+1,j
        elif key == 'd':
            # self.field[i][j] = 'S'
            return i,j+1

# ======================================================================================================

fieldDesign = []
while True:
    subField = [i for i in input().split()]
    if subField == []:
        break
    fieldDesign.append(subField)

s = Saitron(fieldDesign)
hitRecord = []
# Up Side
for i in range(len(s.field[0])):
    ci,cj,cd = 0,i,'s'
    while True:
        cd = s.reflect(ci,cj,cd)
        ci,cj = s.move(ci,cj,cd)
        if ci >= len(s.field) or cj >= len(s.field[0]) or ci < 0 or cj < 0:
            break
    hitRecord.append(s.hit)
    s.hit = 0

# Left Side
for i in range(len(s.field)):
    ci,cj,cd = i,0,'d'
    while True:
        cd = s.reflect(ci,cj,cd)
        ci,cj = s.move(ci,cj,cd)
        if ci >= len(s.field) or cj >= len(s.field[0]) or ci < 0 or cj < 0:
            break
    hitRecord.append(s.hit)
    s.hit = 0

# Down Side
for i in range(len(s.field[0])):
    ci,cj,cd = len(s.field)-1,i,'w'
    while True:
        cd = s.reflect(ci,cj,cd)
        ci,cj = s.move(ci,cj,cd)
        if ci >= len(s.field) or cj >= len(s.field[0]) or ci < 0 or cj < 0:
            break
    hitRecord.append(s.hit)
    s.hit = 0

# Left Side
for i in range(len(s.field)):
    ci,cj,cd = i,len(s.field[0])-1,'a'
    while True:
        cd = s.reflect(ci,cj,cd)
        ci,cj = s.move(ci,cj,cd)
        if ci >= len(s.field) or cj >= len(s.field[0]) or ci < 0 or cj < 0:
            break
    hitRecord.append(s.hit)
    s.hit = 0

print(f"Maximum saitron is {2**(max(hitRecord))} particle(s)")
print()

# s = Saitron()
# ci,cj,cd = 1,1,'s'
# cd = s.reflect(ci,cj,cd)
# ci,cj = s.move(ci,cj,cd)
# print(s)
# print(cd)
# print(ci,cj)
# cd = s.reflect(ci,cj,cd)
# ci,cj = s.move(ci,cj,cd)
# print(s)
# print(cd)
# print(ci,cj)