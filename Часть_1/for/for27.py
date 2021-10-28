import math
print('Вводите ещественное число X и целое число N (> 0)')

x = float(input('X : '))
n = int(input('N : '))

summa = x
fac1 = 2
fac2 = 1

for i in range(3 , n+1) :
    
    if i % 2 == 0 :
        fac1 *= i

    else :
        fac1 *= i
        fac2 *= i-2
        summa += ((x ** i) * fac2 ) / fac1
        fac1 / i 


print(summa)
print(2 + 4/3 + 12/5)
# Programm isn't complete yet. Programm has some error in line 19    