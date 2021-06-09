text = [i for i in input().split()]
# text = 'HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO'.split()
chain = 0
cl = 0
topcl = 0
for i in range(len(text)-1):
    same = 0
    for j in range(len(text[i])):
        if text[i][j] == text[i+1][j]:
            same += 1
    if same >= len(text[i]) -2:
        cl += 1
    else:
        if cl > topcl:
            topcl = cl
        cl = 1
        chain += 1
if cl > topcl:
    topcl = cl
cl = 1
chain += 1

print(f"{chain} Chain(s). Maximum length is {topcl} word(s).")