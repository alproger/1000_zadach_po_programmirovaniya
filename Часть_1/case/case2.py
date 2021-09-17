def switch(number):
    case = {
    
        1 : 'плохо',
        2 : 'неудовлетворительно',
        3 : 'удовлетворительно', 
        4 : 'хорошо',
        5 : 'отлично'

            }
    
    if number in case : 
        result = case[number]
    
    else : result ='ощибка'
    
    return result

print(switch(12))