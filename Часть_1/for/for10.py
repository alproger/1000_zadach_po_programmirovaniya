n = int(input('Вводите целое число N (> 0) : '))
summa = 0
for i in range(1, n+1) :
    summa += 1/i

print(summa)