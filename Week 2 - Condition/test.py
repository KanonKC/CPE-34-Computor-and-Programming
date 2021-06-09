M = input("What's the result of Manchester city's match? ")
L = input("What's the result of Liverpool's match? ")

if M == "won" and L == "lost":
  print("Manchester city is the champion of Premier League.")
elif M == "lost" and L == "won":
  print("Liverpool is the champion of Premier League.")
else:
  mM = input("What is the margin that Manchester city won by? ")
  mL = input("What is the margin that Liverpool city won by? ")
  if mM > mL:
      print("Manchester city is the champion of Premier League.")
  elif mL > mM:
      print("Liverpool is the champion of Premier League.")
  else:
    p = input("Which team won the play-off match?(Manchester city/Liverpool) ")
    if p == "Manchester city":
      print("Manchester city is the champion of Premier League.")
    elif p == "Liverpool":
      print("Liverpool is the champion of Premier League.")