class MyMath:
    def __init__(self):
        pass

    def is_even(self,num):
        if num % 2 == 0:
            return True
        else:
            return False

    def fac(self,num):
        res = 1
        for i in range(2,num+1):
            res *= i
        return res

    def is_prime(self,num):
        isPrime = True
        for i in range(2,num):
            if num % i == 0:
                isPrime = False
                break
        return isPrime

    def divide_by(self,num,k):
        if num % k == 0:
            return True
        else:
            return False
    
    def ten_to_bi(self,num):
        bi = ""
        while num > 0:
            bi = str(num % 2) + bi
            num //= 2
        return bi

    def ten_to_oct(self,num):
        Oct = ""
        while num > 0:
            Oct = str(num % 8) + Oct
            num //= 8
        return Oct

    def ten_to_sixteen(self,num):
        baseNum = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        hexD = ""
        while num > 0:
            hexD = baseNum[(num % 16)] + hexD
            num //= 16
        return hexD
            
    def int_to_roman(self,num):
        Pnum = num
        rs = ""
        i = 0
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roNum = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while Pnum > 0:
            if Pnum >= roNum[i]:
                rs = rs + roman[i]
                Pnum -= roNum[i]
                i = 0
            else:
                i += 1
        return rs
    pi = 3
    for n in range(1,51):
        pi += ((-1)**(n+1))*(4/((n*2 + 1)*(n*2 + 2)*(n*2 + 0)))



my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')