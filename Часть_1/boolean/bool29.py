print("Вводите числа x, y, x 1 , y 1 , x 2 , y 2 ")

print("(x,y)  : ")
x = int(input("x : "))
y = int(input("y : "))
print("(x1,y1)  : ")
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
print("(x2,y2) : ")
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
bol = (x < x1 and y < y1) and (x > x2 and y > y2)
condition = '''Проверить истинность высказыва-
ния: «Точка с координатами (x, y) лежит внутри прямоугольника, левая
верхняя вершина которого имеет координаты (x 1 , y 1 ), правая нижняя —
(x 2 , y 2 ), а стороны параллельны координатным осям».'''
print(condition,bol)
