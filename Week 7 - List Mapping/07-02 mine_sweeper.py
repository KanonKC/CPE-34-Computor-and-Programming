gs = [int(i) for i in input("Grid Size: ").split()]

tmp = gs[0]
gs[0] = gs[1]
gs[1] = tmp


row = gs[0]
col = gs[1]
grid = [[0 for j in range(col)] for i in range(row)]
#print(grid)

nM = int(input("Number of mine(s): "))
bombList = []
for i in range(nM):
    mine = [int(j) for j in input(f"Mine#{i+1}: ").split()]
    tmp = mine[0]
    mine[0] = mine[1]
    mine[1] = tmp

    a = mine[0]
    b = mine[1]
    bombList.append([a,b])
    for j in range(3):
        for k in range(3):
            if mine[0]-1+j < 0 or mine[0]-1+j > row-1 or mine[1]-1+k < 0 or mine[1]-1+k > col-1:
                pass
            else:
                grid[mine[0]-1+j][mine[1]-1+k] += 1
for i in range(nM):
    grid[bombList[i][0]][bombList[i][1]] = "X"

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j],end=" ")
    print()