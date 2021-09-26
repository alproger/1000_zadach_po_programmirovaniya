cost = float(input('Вводите вещественное число — цена 1 кг конфет : '))

for i in range(1,11):
    print(f'{i} кг конфет : ',cost * i)