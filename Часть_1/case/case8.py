day   = int(input('Вводите число  даты : '))
month = int(input('Вводите число  месяца : '))

#1
if month in [1, 3, 5, 7, 8, 10, 12] :
    if day == 31 :
        day, month = 1, month + 1,
        
        if month == 12 :
            month = 1
            print('{}.{}'.format(day, month))

        print('{}.{}'.format(day, month))

    elif day > 31 :
        print('Такой даты нет ')
    
    else :
        day += 1
        print('{}.{}'.format(day, month))

#2    
elif month == 2 :
    if day == 28 :
        day, month = 1, month + 1   
        print('{}.{}'.format(day, month))      

    elif day > 28 :
        print('Такой даты нет ')

    else :
        day += 1
        print('{}.{}'.format(day, month))

#3
elif month in [4, 6, 9, 11] :
    if day == 30 : 
        day, month = 1, month + 1
        print('{}.{}'.format(day, month))

    elif day > 30 : 
        print('Такой даты нет ')

    else :
        day += 1
        print('{}.{}'.format(day, month))
