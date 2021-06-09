t = [i for i in input("Text: ").split()]

chain = 1
maxLength = 0
length = 1
for i in range(len(t)-1):
    same = 0
    for j in range(len(t[i])):
        if t[i][j] == t[i+1][j]:
            same += 1
    if same >= len(t[i])-2:
        length += 1
        #print("SAME",length)
    else:
        if length > maxLength:
            maxLength = length
        #print(length)
        length = 1
        chain += 1
if length > maxLength:
    maxLength = length
#print(length)
# print(maxLength)
# print(chain)
print(f"{chain} Chain(s). Maximum length is {maxLength} word(s).")