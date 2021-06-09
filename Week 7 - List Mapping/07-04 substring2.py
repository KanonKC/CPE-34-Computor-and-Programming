text = input("Text: ")
sub = input("Substring: ")

if sub in text:
    ts = text.split(sub)
    for i in range(len(ts)):
        if i == len(ts)-1:
            print(ts[i],end="")
        else:
            print(ts[i],end="")
            print("[",end="")
            print(sub,end="")
            print("]",end="")

else:
    i = 0
    ts = []
    psud = []
    while i < len(text):
        if text[i] in sub and i <= len(text)-4:
            same = 0
            for j in range(len(sub)):
                if text[i+j] == sub[j]:
                    same += 1
            if same >= len(sub)-1:
                print("[",end="")
                string = ""
                for k in range(len(sub)):
                    if text[i+k] == sub[k]:
                        string = string + sub[k]
                    else:
                        string = string + "?"
                print(string,end="")
                print("]",end="")
                i += len(sub)
            else:
                print(text[i],end="")
                i += 1
        else:
            print(text[i],end="")
            i += 1