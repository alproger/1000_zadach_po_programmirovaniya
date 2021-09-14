print('Вводите четыре целых числа')
num1 = int(input('1-чисел : '))
num2 = int(input('2-чисел : '))
num3 = int(input('3-чисел : '))
num4 = int(input('4-чисел : '))


index = 0

if num1 == num2 and num2 == num3 :
    index = 4

elif num1 == num2 and num2 == num4 :
    index = 3

elif num1 == num3 and num3 == num4:
    index = 2

elif num2 == num3 and num3 == num4 :
    index = 1

print(index)