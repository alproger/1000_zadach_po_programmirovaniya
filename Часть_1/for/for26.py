import math
print('Вводите ещественное число X и целое число N (> 0)')

x = float(input('X : '))
n = int(input('N : '))
summa = 0

for i in range(1 , n+1 , 2) :
    summa  += ( x**i ) / i
    summa *= -1

print(summa)
