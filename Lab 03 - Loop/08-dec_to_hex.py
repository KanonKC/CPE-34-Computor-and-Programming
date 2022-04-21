def hexTrans(num):
    hexN = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    return str(hexN[num])

while True:
    dec = int(input("Input Decimal: "))
    if dec < 0:
        print("Good bye.")
        break
    hexD = ""
    while dec > 0:
        hexD = hexTrans(dec%16) + hexD
        dec = dec // 16
    print(f"Hex: {hexD}")