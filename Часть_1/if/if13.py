print('Вводите три числа ')
num1 = int(input('1-число : '))
num2 = int(input('2-число : '))
num3 = int(input('3-число : '))

num = 0

if num2 > num1 and num1 > num3 or num3 > num1 and num1 > num2 :
    num = num1

elif num1 > num2 and num2 > num3 or num3 > num2 and num2 > num1 :
    num = num2

else:
    num = num3

print(num)