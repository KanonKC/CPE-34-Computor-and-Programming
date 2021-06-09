def 

text = input()
sub = input()

if sub in text:
    ts = text.split(sub)
    for i in range(len(ts)):
        print(ts[i],end="")
        if i!= len(ts)-1:
            print("["+sub+"]",end="")
else:
    for i in range(len(text)-2):
        