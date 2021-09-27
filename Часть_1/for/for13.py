n = int(input('Вводите целое число N (> 0) : '))

summa = 0
k = 1

for i in range(11,(n*10)+1) :
    tsikl = (i/10) * k
    k *= -1 
    summa += tsikl

print(summa)