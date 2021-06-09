a = input("")
aList = a.split(" ")
par = []

for f in aList:
    x = int(f)
    par.append(x)

b = input("")
bList = b.split(" ")
score = []

for g in bList:
    if g == "Ea":
        score.append(-2)
    if g == "Bi":
        score.append(-1)
    if g == "Pa":
        score.append(0)
    if g == "Bo":
        score.append(1)
    if g == "DB":
        score.append(2)

#print(par)
#print(score)

calScore = []
for i in range(0,9,1):
    y = par[i] + score[i]
    calScore.append(y)

print(sum(calScore))