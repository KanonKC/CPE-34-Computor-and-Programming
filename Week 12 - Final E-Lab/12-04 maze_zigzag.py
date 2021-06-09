def printMaze(ans):
    for x in range(len(ans)):
        for y in range(len(ans)):
            print(f'{ans[x][y]:3.0f}',end=' ')
        print()

n = int(input())
maze = [[] for i in range(n)]
num = 1

d1 = n-1
d2 = n-2

harmonic = False
for i in range(n):
    if not harmonic:
        for j in range(d1,d2-i,-1):
            maze[j].append(num)
            num += 1
        harmonic = not harmonic

    else:
        for j in range(d2-i+1,n):
            maze[j].append(num)
            num += 1
        harmonic = not harmonic

for i in range(n):
    if harmonic:
        for j in range(0,d1-i):
            maze[j].append(num)
            num += 1
        harmonic = not harmonic

    else:
        for j in range(d2-i,-1,-1):
            maze[j].append(num)
            num += 1
        harmonic = not harmonic

printMaze(maze)