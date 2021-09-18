month = int(input('Вводите номер месяца — целое число в диапазоне 1–12 : '))

def switch(month):
    
    if month in [1, 3, 5, 7, 8, 12]:
        print('31 дней')

    elif month == 2 :
        print('28-29 дней')
    
    else :
        print('30 дней')


switch(month) 