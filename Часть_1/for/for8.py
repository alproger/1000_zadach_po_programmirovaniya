print('Вводите два целых числа A и B (A < B)')
a = int(input('A : '))
b = int(input('B : '))
pro = 1
for num in range(a, b+1):
    pro *= num 

print(pro)