a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
print(f"Существует треугольник со сторонами {a}, {b}, {c} : ",(a+b>c)and(a+c>b)and(b+c>a))
