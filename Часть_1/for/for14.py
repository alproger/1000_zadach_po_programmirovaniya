n = int(input('Вводите целое число N (> 0) : '))

summa = 0

for i in range(1, 2*n) :
    
    if i % 2 != 0 :
        summa += i

print(summa)