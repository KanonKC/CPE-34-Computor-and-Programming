def decToHex(num,conv=""):
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if num <= 0:
        return conv
    conv = hexa[num % 16] + conv
    return decToHex(num//16,conv)

n = int(input("Input Decimal: "))
print(f"Hex: {decToHex(n)}")