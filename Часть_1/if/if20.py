print('Вводите числовой оси три точки: A, B, C.')
a = int(input('A: '))
b = int(input('B : '))
c = int(input('C : '))

lenght = 0
nearA = 0
if b != c:
    if abs(a-b) < abs(a-c):
        lenght = abs(a-b)
        nearA = f'B({b})'

    else:
        lenght = abs(a-c)
        nearA = f'C({c})'

print(f'точек {nearA} расположена ближе к A, расстояние : {lenght} ')