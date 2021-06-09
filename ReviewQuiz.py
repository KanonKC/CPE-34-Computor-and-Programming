# std_CPE34_63.csv
# notebook_response (1).csv

with open('std_CPE34.csv','r',encoding="utf-8") as std:
    data = [i.strip().split(',') for i in std.readlines()]
    stdData = []
    for i in range(1,len(data)):
        obj = {
            'no': int(data[i][0]),
            'id': int(data[i][1]),
            'name': data[i][2],
            'std': data[i][9]
        }
        stdData.append(obj)
    # print(stdData)

with open('notebook_response (1).csv','r',encoding="utf-8") as note:
    data = [i.strip().split(',') for i in note.readlines()]
    noteData = []
    for i in range(1,len(data)):
        obj = {
            'id': int(data[i][3]),
            'note': data[i][-2],
            'a4': data[i][-1]
        }
        noteData.append(obj)
    # print(noteData)

for i in range(len(stdData)):
    for j in range(len(noteData)):
        if stdData[i]['id'] == noteData[j]['id']:
            stdData[i]['note'] = noteData[j]['note']
            stdData[i]['a4'] = noteData[j]['a4']
            break
    else:
        stdData[i]['note'] = None
        stdData[i]['a4'] = None

for i in range(len(stdData)):
    print(stdData[i]['note'])