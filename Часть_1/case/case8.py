day   = int(input('Вводите число  даты : '))
month = int(input('Вводите число  месяца : '))

#1
if month in [1, 3, 5, 7, 8, 10, 12] :
    if day == 1 :
        day, month  = 30, month -1
        print('{}.{}'.format(day, month))

        if month == 1 :
            day, month = 31, 12
            print('{}.{}'.format(day, month))
        
        elif month == 3 :
            day, month = 28, 2
            print('{}.{}'.format(day, month))
   
    elif day > 31 :
        print('Такой даты нет ')

    else :
        day -= 1
        print('{}.{}'.format(day, month))
    
elif month == 2 :
    if day == 1 :
        day, month = 31, 1
        print('{}.{}'.format(day, month))

    elif day > 31 :
        print('Такой даты нет ')

    else :
        day -= 1
        print('{}.{}'.format(day, month))

elif month in [4, 6, 9, 11] :
    if day == 1 : 
        day, month = 31, month - 1
        print('{}.{}'.format(day, month))

    elif day > 30 : 
        print('Такой даты нет ')

    else :
        day -= 1
        print('{}.{}'.format(day, month))
