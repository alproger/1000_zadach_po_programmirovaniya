print('Вводите три целых числа')
num1 = int(input('1-число : ')) 
num2 = int(input('2-число : '))
num3 = int(input('3-число : '))

count1, count2 = 0,0

if num1 > 0 : 
    count1 += 1
elif num1 < 0:
    count2 += 1

if num2 > 0 :
    count1 += 1
elif num2 < 0:
    count2 += 1

if num3 > 0 :
    count1 += 1
elif num3 < 0:
    count2 += 1

print(f' количество положительные : {count1} \
\n количество отрецательные : {count2} ')