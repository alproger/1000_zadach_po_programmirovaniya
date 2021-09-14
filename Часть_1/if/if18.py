print('Вводите три числа')
num1 = int(input('1-чисел : '))
num2 = int(input('2-чисел : '))
num3 = int(input('3-чисел : '))

index = 0

if num1 == num2 :
    index = 3

elif num1 == num3:
    index = 2

elif num2 == num3:
    index = 1

print(index)