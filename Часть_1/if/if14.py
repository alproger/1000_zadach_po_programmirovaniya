print('Вводите три числа ')
num1 = int(input('1-число : '))
num2 = int(input('2-число : '))
num3 = int(input('3-число : '))

min_num, max_num = 0, 0 
if num1 != num2 and num2 != num3 :
    if num1 > num2 and num1 > num3 :
        max_num = num1
    elif num1 < num2 and num1 < num3 : 
        min_num = num1
    
    if num2 > num1 and num2 > num3 :
        max_num = num2
    elif num2 < num1 and num2 < num3 :
        min_num = num2

    if num3 > num1 and num3 > num2 :
        max_num = num3
    elif num3 < num1 and num3 < num2 :
        min_num = num3
else :
    print('oops!')
print(f'наименьшее : {min_num} \nнаибольшее : {max_num}')

