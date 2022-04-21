size = [int(i) for i in input("City Size: ").split()]
row = size[0]
col = size[1]

cityMap = [[int(j) for j in input().split()] for i in range(row)]

direction = {
    "N":0,
    "S":0,
    "E":0,
    "W":0
}

# NORTH
for i in range(col):
    front = 0
    for j in range(row):
        if cityMap[j][i] > front:
            direction["N"] += 1
            front = cityMap[j][i]

# SOUTH
for i in range(col):
    front = 0
    for j in range(row-1,-1,-1):
        if cityMap[j][i] > front:
            direction["S"] += 1
            front = cityMap[j][i]

# EAST
for i in range(row):
    front = 0
    for j in range(col-1,-1,-1):
        if cityMap[i][j] > front:
            direction["E"] += 1
            front = cityMap[i][j]

# WEST
for i in range(row):
    front = 0
    for j in range(col):
        if cityMap[i][j] > front:
            direction["W"] += 1
            front = cityMap[i][j]

most = max(direction.values())
for i in direction:
    if direction[i] == most:
        print(i,end=" ")