class Hanabi:
    def __init__(self,s):
        self.sky = [['.' for j in range(s)] for i in range(s)]
    
    def __str__(self):
        formatString = ""
        for i in range(len(self.sky)):
            for j in range(len(self.sky[0])):
                formatString += str(self.sky[i][j]) + " "
            formatString += '\n'
        return formatString

    def addFistFirework(self,x,y,n):
        control = (n-1)//2
        fire = []
        for i in range(control):
            subFire = '.'*i + '1' + '.'*(control-i-1) + '1' + '.'*(control-i-1) + '1'
            fire.append([subFire[j] for j in range(len(subFire))])
        fire.append(['1' for i in range(n)])
        for i in range(control):
            subFire = ' '*(control-i-1) + '1' + ' '*(i) + '1' + ' '*(i) +'1'
            fire.append([subFire[j] for j in range(len(subFire))])

        for i in range(len(fire)):
            for j in range(len(fire[i]),len(fire[0])):
                fire[i].append('.')

        # Draw
        center = (n-1)//2
        sx = x - center
        sy = y - center

        for i in range(n):
            for j in range(n):
                if fire[i][j] == '.':
                    pass
                else:
                    try:
                        self.sky[sx+i][sy+j] += int(fire[i][j])
                    except TypeError:
                        self.sky[sx+i][sy+j] = fire[i][j]
                    except ValueError:
                        self.sky[sx+i][sy+j] = '.'
                    except IndexError:
                        pass

    def addSecondFirework(self,x,y,n):
        # x += 1
        # y += 1
        num = n
        fire = [[0 for j in range(n*2-1)] for i in range(n*2-1)]
        row = len(fire)
        col = len(fire[0])
        
        for i in range(n):
            
            # Up
            for j in range(col):
                if fire[i][j] > 0:
                    pass
                else:
                    fire[i][j] += num
            
            # Left
            for j in range(row):
                if fire[-j-1][i] > 0:
                    pass
                else:
                    fire[-j-1][i] += num

            # Right
            for j in range(row):
                if fire[-j-1][-i-1] > 0:
                    pass
                else:
                    fire[-j-1][-i-1] += num

            # Down
            for j in range(col):
                if fire[-i-1][j] > 0:
                    pass
                else:
                    fire[-i-1][j] += num
                
            num -= 1
        # print(fire)

        # Draw
        center = n-1
        sx = x - center
        sy = y - center

        for i in range(n*2-1):
            for j in range(n*2-1):
                try:
                    self.sky[sx+i][sy+j] += fire[i][j]
                except TypeError:
                    self.sky[sx+i][sy+j] = fire[i][j]
                except IndexError:
                    pass

    def oneDigit(self):
        for i in range(len(self.sky)):
            for j in range(len(self.sky[0])):
                if len(str(self.sky[i][j])) > 1:
                    self.sky[i][j] = str(self.sky[i][j])[-1]

h = Hanabi(int(input('Sky : ')))

for i in range(int(input('Hanabi : '))):
    f = [int(i) for i in input().split()]
    if f[2] == 1:
        h.addFistFirework(f[0],f[1],f[3])
    if f[2] == 2:
        h.addSecondFirework(f[0],f[1],f[3])
    # print(h)

h.oneDigit()
print(h)
