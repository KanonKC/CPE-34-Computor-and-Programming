mthMan = input("What's the result of Manchester city's match? ")
mthLiv = input("What's the result of Liverpool's match? ")

if mthMan == "won" and mthLiv == "lost":
    print("Manchester city is the champion of Premier League.")
elif mthMan == "lost" and mthLiv == "won":
    print("Liverpool is the champion of Premier League.")
else:
    mgnMan = int(input("What is the margin that Manchester city won by? "))
    mgnLiv = int(input("What is the margin that Liverpool won by? "))
    if mgnMan > mgnLiv:
        print("Manchester city is the champion of Premier League.")
    elif mgnMan < mgnLiv:
        print("Liverpool is the champion of Premier League.")
    else:
        playoff = input("Which team won the play-off match?(Manchester city/Liverpool) ")
        if playoff == "Manchester city":
            print("Manchester city is the champion of Premier League.")
        else:
            print("Liverpool is the champion of Premier League.")





