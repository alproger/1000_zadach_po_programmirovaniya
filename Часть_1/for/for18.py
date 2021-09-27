a = int(input('Вводите вещественное число A (> 0) : '))
n = int(input('Вводите целое число N (> 0) : '))

summa  = 0

for i in range(0, n+1) :
    summa += (-a) ** i 

print(summa)
