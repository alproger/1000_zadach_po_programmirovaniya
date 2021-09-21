command = int(input(''' Выберите следующие команды 
1 — радиус R, 
2 — диаметр D, 
3 — длина L , 
4 — площадь круга S 
> '''))

commands = {
1 : 'радиус R', 
2 : 'диаметр D ', 
3 : 'длина L ', 
4 : 'площадь круга '
           }
           
if command in commands.keys():
    value = float(input('Вводите значия  {} : '.format(commands[command])))
    if command == 1 :
        R = value  
        D = 2 *  R 
        L = 2 * 3.14 * R 
        S = 3.14 * (R ** 2)
        print(f'радиус R = {R} \nдиаметр D = {D} , \nдлина L = {L},\nплощадь круга S = {S} ')

    elif command == 2 :
        D = value 
        R = D/2
        L = 2 * 3.14 * R  
        S = 3.14 * (R ** 2)
        print(f'радиус R = {R} \nдиаметр D = {D} , \nдлина L = {L},\nплощадь круга S = {S} ')

    elif command == 3 :
        L = value 
        R = value/(3.14 * 2) 
        D = 2 * R 
        S = 3.14 * (R ** 2)
        print(f'радиус R = {R} \nдиаметр D = {D} , \nдлина L = {L},\nплощадь круга S = {S} ')

    elif command == 4 :
        S = value 
        R = ((value/ 3.14) ** 1/2) 
        D = 2 * R
        L = 3.14 * D
        print(f'радиус R = {R} \nдиаметр D = {D} , \nдлина L = {L},\nплощадь круга S = {S} ')
    
else : 
    print('Такого команда нет!')
