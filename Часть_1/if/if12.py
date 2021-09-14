print('Вводите 3 числа : ')
num1 = int(input('1-чисел : '))
num2 = int(input('2-чисел : '))
num3 = int(input('3-чисел : '))

min_num = 0
if num1 < num2 and num1 < num3 : 
    min_num = num1

elif num2 < num1 and num2 < num2 :
    min_num = num2

else:
    min_num = num3

print(f'Наименшое число : {min_num} ')