year = int(input('Вводите целое число в диапазоне 10-40 : '))

ones = {

    1 : 'один одно учебное задание ',
    2 : 'два учебных задания',
    3 : 'три учебных задания',
    4 : 'четыре учебных задания',
    5 : 'пятть учебных заданий',
    6 : 'шесть учебных заданий',
    7 : 'семь учебных заданий',
    8 : 'восемь учебных заданий',
    9 : 'девять учебных заданий'    

                       }

tens = {
    10 : 'Десять',
    20 : 'Двадцать',
    30 : 'Тридцать',
    40 : 'Сорок'
   

}

ten = int((year // 10) * 10)
one = int(year % 10)

if ten  in tens.keys() :
    message = tens[ten]
    
    if one in ones.keys() :
        message += f'  {ones[one]}' 

    else :
        message += ' учебных заданий '

    print(message)    

else :
    if one in ones.keys() :
        message = f' {ones[one]}'

        print(message)





