n = int(input('n: '))
control = (n-1)//2

for i in range(control):
    print(' '*i + '+' + ' '*(control-i-1) + '+' + ' '*(control-i-1) + '+')
print('+'*n)
for i in range(control):
    print(' '*(control-i-1) + '+' + ' '*(i) + '+' + ' '*(i) +'+')