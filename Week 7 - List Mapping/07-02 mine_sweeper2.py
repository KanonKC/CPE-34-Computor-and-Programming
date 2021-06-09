def printField(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j],end="  ")
        print()

grid = [int(i) for i in input("Grid Size: ").split()]

field = [[0 for j in range(grid[0])] for i in range(grid[1])]

nMine = int(input("Number of mine(s): "))
a = 1
recMine = []
while nMine >= a:
    mine = [int(i) for i in input(f"Mine #{a}:").split()]
    row,col = mine[0],mine[1]
    recMine.append(mine)
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            try:
                field[i][j] += 1
            except IndexError:
                pass
    a += 1

for i in range(len(recMine)):
    field[recMine[i][0]][recMine[i][1]] = "X"

printField(field)