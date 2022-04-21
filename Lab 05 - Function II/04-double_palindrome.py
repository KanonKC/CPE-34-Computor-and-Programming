text = str(input("Text: "))
t = text.upper()

def isPal(text):
    Pal = True
    for i in range(len(text)):
        if text[i] != text[-i-1]:
            return False
    if Pal:
        return True

if len(t) % 2 == 0: # IS EVEN
    ts1 = t[slice((len(t)//2))]
    ts2 = t[slice(len(t)//2,len(t)+1)]
else: # IS ODD
    ts = t.split(t[(len(t)//2)])
    ts1 = ts[0]
    ts2 = ts[1]

#print(ts1,ts2)

p = 0
if isPal(t):
    p += 1
    if isPal(ts1) and isPal(ts2):
        p += 1

if p == 1:
    print("Palindrome")
elif p == 2:
    print("Double Palindrome")
else:
    print("No")