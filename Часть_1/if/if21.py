print('Вводите целочисленные координаты точки(x,y) на плоскости ')
x = int(input('x : '))
y = int(input('y : '))

result  = 0
if x and y == 0:
    result = 0

elif x == 0 and y != 0 or x != 0  and y == 0 :
    result = 1

elif x and y != 0:
    result = 3
print(result)