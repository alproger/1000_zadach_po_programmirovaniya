n = int(input('Вводите целое число N (> 0) : '))
summa = 0

for i in range(n, (2*n)+1) :
    summa += (i ** 2)


print(summa)