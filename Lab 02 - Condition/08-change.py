chg = int(input())

bank1000 = chg / 1000
chg = chg % 1000

bank500 = chg /500
chg = chg % 500

bank100 = chg /100
chg = chg % 100

bank50 = chg /50
chg = chg % 50

bank20 = chg /20
chg = chg % 20

coin10 = chg /10
chg = chg % 10

coin5 = chg /5
chg = chg % 5

coin1 = chg /1
chg = chg % 1

print("1000 =>",int(bank1000))
print("500 =>",int(bank500))
print("100 =>",int(bank100))
print("50 =>",int(bank50))
print("20 =>",int(bank20))
print("10 =>",int(coin10))
print("5 =>",int(coin5))
print("1 =>",int(coin1))