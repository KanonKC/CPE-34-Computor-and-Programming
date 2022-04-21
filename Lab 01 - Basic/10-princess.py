s = int(input("s: "))

m = min = s / 60
sec = s%60

min = m%60
hour = m/60


print(s,"seconds equals",int(hour),"hour(s)",int(min),"minute(s)","and",sec,"second(s)")