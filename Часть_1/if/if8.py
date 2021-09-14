print('Вводите 2 целых числа')
num1 = int(input('1-число : ')) 
num2 = int(input('2-число : '))

print(f'{num1} \n{num2}') if num1 > num2 else print(f'{num2} \n{num1}')