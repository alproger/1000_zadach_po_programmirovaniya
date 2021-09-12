a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d  = (b**2) - 4*a*c
if(d<0): print("нет корней")
elif(d==0):
    x = -b/(2*a)
    print("x = ",x)
else:
    x1 = (-b + d)/2*a
    x2 = (-b - d)/2*a
    print("x1 : ",x1 ,"\n x2 : ",x2)


