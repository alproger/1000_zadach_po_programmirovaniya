a = int(input("a : "))
b = int(input("b : "))
temp = b
if a>b :
    b = a
    a = temp
elif b>a :
    b = a
    a = temp

print("a : ",a)
print("b : ",b)