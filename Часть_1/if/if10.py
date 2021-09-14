
a = int(input("a : "))
b = int(input("b : "))
temp = 0
if a!=b :
    temp = a+b
    a = temp
    b = a
elif a==b :
    a = 0
    b = 0
    
print("a : ",a)
print("b : ",b)



