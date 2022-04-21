min = int(input("How long have Buzz played ?: "))

hour = min // 60
#print(hour)
minl = min % 60
#print(minl)

if minl > 20:
    hour += 1
#print(hour)

cost = hour*900

#print(cost)

if hour >= 2 and hour < 4: # 2 - 4 Hour
    cost = (cost * 9)/10
elif hour >= 4 and hour < 5: # 4 Hour
    cost = (cost * 8)/10
elif hour >= 5:
    cost = (cost * 7)/10

#print(cost)
print("Total price is %d baht." % cost)