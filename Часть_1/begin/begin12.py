print("Вводите катеты прямоугольного треугольника a и b : ")
a = int(input("a : "))
b = int(input("b : "))
c = pow((pow(a,2)+pow(b,2)),1/2)
p = a+b+c
print("гипотенуза c : ",c)
print("периметр p : ", p)
