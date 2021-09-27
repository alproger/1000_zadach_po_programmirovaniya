a = int(input('Вводите вещественное число A (> 0) : '))
n = int(input('Вводите целое число N (> 0) : '))

for i in range(1, n+1) :
    print(f'{a}^{i} = ', a ** i)