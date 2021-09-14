print('Вводите координаты точки, не лежащей на координатных осях OX и OY')
x = int(input('x : '))
y = int(input('y : '))

position = 0

if x and y != 0:

    if x  and y > 0 :
        position = 1
    
    elif x < 0 and y > 0 :
        position = 2
    
    elif x and y < 0 :
        position = 3

    elif x > 0 and y < 0 :
        position = 4
    

print(f'номер координатной четверти, в которой находится данная точка : {position}')