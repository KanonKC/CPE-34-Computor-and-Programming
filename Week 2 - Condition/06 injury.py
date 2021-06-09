etime = int(input("Estimated time : "))
hreq = etime * 2.5
time = etime // 8

i = 1

tpt = 0
twt = 0
tft = 0

while i <= time:
    print(f"Week{i}")
    pt = int(input("Physical therapy : "))
    wt = int(input("Weight training : "))
    ft = int(input("Fitness training : "))
    tpt += pt
    twt += wt
    tft += ft
    if tpt >= hreq and twt >= hreq and tft >= hreq:
        print("Buzzy has recovered in time.")
        break
    i += 1

if tpt < hreq and twt < hreq and tft < hreq:
    print("Buzzy has not recovered in time.")

