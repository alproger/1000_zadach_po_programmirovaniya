print("Вводите координаты двух различных полей шахматной доски x 1 , y 1 ,x 2 , y 2 (целые числа, лежащие в диапазоне 1–8): ")
x = int(input("x : "))
y = int(input("y : "))
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
print("Ладья за один ход может перейти с одного поля на другое : ",(x==x1 and y!=y1)or(x!=x1 and y==y1))
