lenght = float(input('Вводите длина отрезка : '))

print('''Вводите тип этого длина отрезка  
    1 : дециметр,
    2 : километр, 
    3 : метр, 
    4 : миллиметр, 
    5 : сантиметр  ')
''')

type_lenght = int(input(" : "))

def switch(argument,type_argumet):
    result = 0
    if type_argumet == 1 :
        result = argument/10
        
    elif type_argumet == 2 : 
        result = argument * 1000
        
    elif type_argumet == 3 : 
        result = argument * 1

    elif type_argumet == 4 :
        result = argument * 0.001
        
    elif type_argumet == 5 :
        result = argument / 100
    
    return result


print(switch(lenght,type_lenght))


