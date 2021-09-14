print('Вводите три числа ')
num1 = int(input('1-число : '))
num2 = int(input('2-число : '))
num3 = int(input('3-число : '))

sum_num = 0
if num1 < num2 and num1 < num3 :
    sum_num = num2 + num3
elif num2 < num1 and num2 < num3 :
    sum_num = num1 + num3
else :
    sum_num = num1 + num2

print(f'суммa двух наибольших из них : {sum_num}')
