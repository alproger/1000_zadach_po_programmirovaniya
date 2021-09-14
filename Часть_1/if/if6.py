print('Вводите 2 целых числа')
num1 = int(input('1-число : ')) 
num2 = int(input('2-число : '))

max_num = num1 if num1> num2 else num2
print(f'Большое число : {max_num}')