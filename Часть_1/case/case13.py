command = int(input('''
Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом: 
1 — катет a, 
2 — гипотенуза 
c = a· 2, 
3 — высота h, опущенная на гипотенузу (h = c/2), 
4 — площадь S = c·h/2
Вводите один из них :  '''))

types = {
        1 : 'катет a ', 
        2 : 'гипотенуза c', 
        3 : 'высота h',  
        4 : 'площадь S'
           }

if command in types.keys():
    value = float(input('Вводите значения {} : '.format(types[command])))
    
    a, c, h, S = 0, 0, 0, 0
    
    if command == 1 :
        a = value
        c =  a * (2 ** 1/2)
        h =  c / 2
        S = c* h / 2

    elif command == 2 :
        c = value
        a =  c / (2 ** 1/2)
        h =  c / 2
        S = c * h / 2
    
    elif command == 3 :
        h = value
        c = 2 * h
        a = c / (2 ** 1/2)
        S = c* h / 2

    elif command == 3 :
        S = value
        c =  S ** 1/2
        h =  c / 2
        a = c / (2 ** 1/2)
    
    print(f'катет a = {a} \nгипотенуза c = {c} \nвысота h = {h} \nплощадь S = {S}')


else :
    print('Такого команды нет')