# 1) [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]
print([i for i in range(20,8,-1)])

# 2) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,121, 144]
print([i**2 for i in range(1,13)])

# 3) [-1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25]
print([((i*2)-1)*((-1)**i) for i in range(1,14)])

# 4) [1, 3, 6, 10, 15, 21, 28, 36, 45]
print([sum(list(range(1,(i+1)))) for i in range(1,10)])

# 5) ['*', '***', '*****', '*******', '*********']
print(["*"*((i*2)-1) for i in range(1,6)])
