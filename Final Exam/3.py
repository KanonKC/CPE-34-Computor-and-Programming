# MAIN DATA STRUCTURE ===================================

data = []
with open('out1.csv') as f:
    rawData = [i.strip().split(',') for i in f.readlines()]
    for i in range(1,len(rawData)):
        obj = {
            'Name': rawData[i][0],
            'Platform': rawData[i][1],
            'License': rawData[i][2],
            'NbOfVersion': int(rawData[i][3]),
            'Language': rawData[i][4],
            'Host': rawData[i][5],
            'Size': float(rawData[i][6]),
            'Stars': int(rawData[i][7]),
            'ReadmeFilename': rawData[i][8]
        }
        data.append(obj)

# CUSTOM STRUCTURE ======================================
platCount = {} # Platform Counter
for i in range(len(data)):
    ptf = data[i]['Platform']
    if ptf in platCount:
        platCount[ptf] += 1
    else:
        platCount[ptf] = 1

licCount = {} # License Counter
for i in range(len(data)):
    lic = data[i]['License']
    if lic in licCount:
        licCount[lic] += 1
    else:
        licCount[lic] = 1

# { Name : Version }
version = {data[i]['Name']:data[i]['NbOfVersion'] for i in range(len(data))}

pyFileList = [] # List of All File Size that wrote by Python
for i in range(len(data)):
    if data[i]['Language'] == "Python":
        pyFileList.append(data[i]['Size'])

gitLangCount = {} # Language Counter for GitHub
for i in range(len(data)):
    if data[i]['Host'] == "GitHub":
        if data[i]['Language'] in gitLangCount:
            gitLangCount[data[i]['Language']] += 1
        else:
            gitLangCount[data[i]['Language']] = 1

# COMMAND ===========================================

def c1():
    print(f"Total Platform: {len(platCount)}")

    # Find 1st
    mostPlat = ['',0]
    for i in platCount:
        if platCount[i] > mostPlat[1]:
            mostPlat[1] = platCount[i]
            mostPlat[0] = i

    # Find 2nd
    secPlat = ['',0]
    for i in platCount:
        if platCount[i] > secPlat[1] and platCount[i] < mostPlat[1]:
            secPlat[1] = platCount[i]
            secPlat[0] = i

    print(f"1st Most Used Platform: {mostPlat[0]} ({mostPlat[1]})")
    print(f"2nd Most Used Platform: {secPlat[0]} ({secPlat[1]})")

def c2():
    print(f"Total License: {len(licCount)}")

    # Find 1st
    mostLic = ['',0]
    for i in licCount:
        if licCount[i] > mostLic[1]:
            mostLic[1] = licCount[i]
            mostLic[0] = i

    # Find 2nd
    secLic = ['',0]
    for i in licCount:
        if licCount[i] > secLic[1] and licCount[i] < mostLic[1]:
            secLic[1] = licCount[i]
            secLic[0] = i
    
    print(f"1st Most Used License: {mostLic[0]} ({mostLic[1]})")
    print(f"2nd Most Used License: {secLic[0]} ({secLic[1]})")

def c3():
    # Find Most Version
    mostVer = ['',0]
    for i in version:
        if version[i] > mostVer[1]:
            mostVer[0] = i
            mostVer[1] = version[i]
    print(f"Lasted Version Updated: {mostVer[1]}")
    print(f"Project Name: {mostVer[0]}")

def c4():
    totalSize = 0
    for i in range(len(pyFileList)):
        totalSize += pyFileList[i]
    print(f"Averange File Size for Python Project: {totalSize/len(pyFileList):.3f} (MB)")

def c5():
    leastLang = 9999999999
    for i in gitLangCount:
        if gitLangCount[i] < leastLang:
            leastLang = gitLangCount[i]
    
    leastLangName = ""
    leastLangCount = 0
    for i in gitLangCount:
        if gitLangCount[i] == leastLang:
            leastLangName += i + ', '
            leastLangCount += 1


    print(f"Least Used Language: {leastLangCount} ({leastLangName})")
    print(f'Total Project that Use "Least Used Language": {leastLangCount * leastLang}')

# UI =====================================================

while True:
    command = input("(Enter 1,2,3,4 or 5): ")
    try:
        exec(f'c{command}()')
    except Exception:
        pass