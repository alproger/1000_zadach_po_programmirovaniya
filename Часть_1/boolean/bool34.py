print(Вводите координаты поля шахматной доски x, y (целые числа, лежащие в диапазоне 1–8)")
x = int(input("x : "))
y = int(input("y : "))
print("Данное поле является белым: ",(x+y)%2!=0)
