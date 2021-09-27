import math
print('Вводите ещественное число X и целое число N (> 0)')

x = float(input('X : '))
n = int(input('N : '))

sum_fac = 0

for i in range(1 , n+1 , 2) :
    sum_fac  += x**i / math.factorial(i)
    sum_fac *= -1

print(sum_fac)
