print('Вводите два целых числа A и B (A < B)')
a = int(input('A : '))
b = int(input('B : '))

for num in range(b, a-1, -1):
    print(num, end=' ')


print('\nN : ',len(range(a,b+1)))
