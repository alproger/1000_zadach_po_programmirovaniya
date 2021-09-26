cost = float(input('Вводите вещественное число — цена 1 кг конфет : '))

for i in range(1,11):
    result = f'{i/10} кг конфет стоит : {(i/10) * cost}'
    print(result)