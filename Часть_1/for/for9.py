print('Вводите два целых числа A и B (A < B)')
a = int(input('A : '))
b = int(input('B : '))
summa = 0
for num in range(a, b+1):
    summa += (num ** 2)  

print(summa)