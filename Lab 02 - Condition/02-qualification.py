w = int(input("Weight: "))
h = int(input("Height: "))

b = w / (h/100)**2

if b < 18.6:
    print("Your BMI is %.1f You're in the underweight range." % b)
elif b >= 18.6 and b < 25:
    print("Your BMI is %.1f You're in the healthy weight range." % b)
elif b >= 25 and b < 30:
    print("Your BMI is %.1f You're in the overweight range." % b)
else:   
    print("Your BMI is %.1f You're in the obese range." % b)


#    print("Your BMI is %.2f You're in the " % b)