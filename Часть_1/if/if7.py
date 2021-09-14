print('Вводите 2 целых числа')
num1 = int(input('1-число : ')) 
num2 = int(input('2-число : '))

min_num_index = 1 if num1 < num2 else 2
print(f' номер меньшего : {min_num_index}')