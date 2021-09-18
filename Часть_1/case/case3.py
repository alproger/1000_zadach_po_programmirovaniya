month = int(input('Вводите номер месяца — целое число в диапазоне 1–12 : '))

def switch(month):

    case = {
        'winter' : 'Зима',
        'spring' : 'Весна',
        'summer' : 'Лето',
        'autmn'  : 'Осень'    }

    if month in [1, 2, 12] :
        print(case['winter'])
    
    elif month in [3, 4, 5] :
        print(case['spring'])

    elif month in [6, 7, 8] :
        print(case['summer'])

    elif     month in [9, 10, 11] :
        print(case['autmn'])    
    

switch(month) 