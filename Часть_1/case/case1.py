def switch_number(number):
    
    case = {
        1 : 'Понидельник',
        2 : 'Вторник',
        3 : 'Среда',
        4 : 'Четверг',
        5 : 'Пятница',
        6 : 'Суббота',
        7 : 'Воскресения',
           }
    
    if number in case:
        return case[number]

    else : return 'not found !'
print(switch_number(11))