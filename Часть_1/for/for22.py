print('Вводите ещественное число X и целое число N (> 0)')

x = float(input('X : '))
n = int(input('N : '))

factorial = 1
summa = 1

for i in range(1,n+1) :
    factorial *= i
    summa += (x ** i) / factorial 

print(summa)