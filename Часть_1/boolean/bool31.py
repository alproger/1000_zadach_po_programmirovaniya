a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
print(f" реугольник со сторонами {a}, {b}, {c} является равнобедренным : ",(a==b  and b!=c)or(a==c and a==b)or(b==c and b!=a))
