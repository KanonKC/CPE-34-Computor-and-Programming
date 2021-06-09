def printMiniSodoku(a):
    res,n = '',len(a)
    for i in range(n):
        for j in range(n):
            res += f'{a[i][j]:3}'
        if i < n-1:
            res += '\n'
    print(res)

def readMiniSodoku(a):
    with open(a,'r') as f:
        c = [i.strip().split(',') for i in f.readlines()]
        return c

def printSubGrid(a):
    subG = ""
    qa = int(len(a)**(0.5))
    for i in range(qa):
        for j in range(qa*i,qa*i+qa):
            subG = subG + a[j] + " "
        if i < qa-1:
            subG = subG + "\n"
    return subG

def checkMiniSodoku(a):
    fail = False
    subRow = int(len(a)**(0.5))
    data = []
    for l in range(subRow):
        for k in range(subRow):
            sub = []
            for i in range(subRow*l,subRow*l+subRow):
                for j in range(subRow*k,subRow*k+subRow):
                    sub.append(a[i][j])
            data.append(sub)

    # cloneData = [i for i in data]
    for i in range(len(data)):
        c = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                c += 1
        if c > 1:
            fail = True
            print(f"fails test#2!")
            # print(data[i])
            return printSubGrid(data[i])
            break

    if not fail:
        for i in range(len(data)):
            num = [str(i+1) for i in range(len(a))]
            for j in range(len(data)):
                if data[i][j] in num:
                    num.remove(data[i][j])
                else:
                    fail = True
                    print(f"fail test#1!")
                    # print(data[i])
                    return printSubGrid(data[i])
                    break

    if not fail:
        return "True"

# ================================================================
fn = "Minisodoku06.txt" # input('Enter Minisodoku0X.txt: ')
s = readMiniSodoku(fn)
print('Running Sudoku')
printMiniSodoku(s) # Pass
res = checkMiniSodoku(s)
print(res)