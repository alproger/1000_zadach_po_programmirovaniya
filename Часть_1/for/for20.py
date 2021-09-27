
n = int(input('Вводите целое число N (> 0) : '))
factorial  = 1
summa = 0

for i in range(1, n+1) :
    factorial *= i  
    summa += factorial

print(summa)

