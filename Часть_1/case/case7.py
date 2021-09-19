massa = float(input('Вводите масса тела :'))
print('''Вводите Единицы массы пронумерованы следующим образом: 
1 — килограмм,
2 — миллиграмм, 
3 — грамм, 
4 — тонна, 
5 — центнер.''')

type_mass = int(input('Единица массу : '))

def switch(argument, type_argument):
    result = 0
    
    if type_argument == 1 :
        result = argument
    
    elif type_argument == 2 :
        result = argument * 1e-6
    
    elif type_argument == 3 :
        result = argument * 0.001

    elif type_argument == 4 : 
        result = argument * 1000

    elif type_argument == 5 :
        result = argument * 100

    return result

print(switch(massa, type_mass))
