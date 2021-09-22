year = int(input('Вводите целое число в диапазоне 20-69 : '))

ones = {

    1 : 'один ',
    2 : 'два ',
    3 : 'три ',
    4 : 'четыре ',
    5 : 'пятть ',
    6 : 'шесть ',
    7 : 'семь ',
    8 : 'восемь ',
    9 : 'девять '    

                       }

tens = {
    10 : 'Десять',
    20 : 'Двадцать',
    30 : 'Тридцать',
    40 : 'Сорок',
    50 : 'Пятьдесят',
    60 : 'Шестьдесят'

}

ten = int((year // 10) * 10)
one = int(year % 10)

if ten  in tens.keys() :
    message = tens[ten]
    
    if one in ones.keys() :
        message += f'  {ones[one]}' 


    print(message)    

else :
    if one in ones.keys() :
        message = f' {ones[one]}'

        print(message)





