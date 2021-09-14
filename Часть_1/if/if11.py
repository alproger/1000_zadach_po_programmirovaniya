print('Вводите 2 переменные целого типа : ')
num1 = int(input('1-чисел : '))
num2 = int(input('2-чисел : '))

if num1 == num2 : 
    num1,num2 = 0,0
else:
   if num1 > num2 :
       num2 = num1
   else:
       num1 = num2

print(num1,'\n',num2) 