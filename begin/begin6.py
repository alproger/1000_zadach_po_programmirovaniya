print('Вводите длины ребер a, b, c')
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
v = a * b * c
s = 2 * ((a*b) + (b*c) + (a*c))
print('объем куба : ', v)
print('площадь поверхности куба : ', s)
