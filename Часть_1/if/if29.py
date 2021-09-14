num = int(input('Вводите целое число : '))
if num < 0 :
    print('отрицательное ', end= '')
    if num % 2 == 0:
        print('четное число')
    else:
        print('нечетное число')

elif num == 0 :
    print('нулевое число')

elif num > 0 :
    print('положительное ', end='')
        
    if num % 2 == 0:
        print('четное число')
    else:
        print('нечетное число')

