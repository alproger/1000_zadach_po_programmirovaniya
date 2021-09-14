print('Вводите три числа A, B, C ')
a = int(input('A : '))
b = int(input('B : '))
c = int(input('C : '))

if (a < b and b < c) or (a > b and b > c) :
    a *= 2
    b *= 2
    c *= 2
else :
    a *= -1
    b *= -1
    c *= -1

print(f'{a}\n{b}\n{c}')