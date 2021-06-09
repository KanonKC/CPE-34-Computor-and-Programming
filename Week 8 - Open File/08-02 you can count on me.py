f = open("input.txt","r")
cont = f.read()
con = cont.split()
sen = cont.split(".")
f.close()

word = {}
for i in range(len(con)):
    if con[i] in word:
        word[con[i]] += 1
    else:
        word[con[i]] = 1

c = 0
for i in word:
    c += word[i]

print(len(sen))