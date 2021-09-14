int_number = int(input('Вводите целое число : '))

if int_number > 0 :
    int_number += 1

elif int_number < 0:
    int_number -= 2

else:
    int_number = 10

print(int_number)