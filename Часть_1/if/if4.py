print('Вводите три целых числа')
num1 = int(input('1-число : ')) 
num2 = int(input('2-число : '))
num3 = int(input('3-число : '))

count = 0

if num1 > 0 : 
    count += 1
if num2 > 0 :
    count += 1
if num3 > 0 :
    count += 1
print(f' количество положительные : {count}')