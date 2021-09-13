print("shaxmat doskasidai kordinatani kiriting \n ot kordinatasi : ")
x = int(input("x : "))
y = int(input("y : "))
print("ot o'tishi kerak bo'lgan kordinata : ")
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
shart = ((x+1==x1 and (y+2==y1) or (y-2==y1)) or (x-1==x1 and (y+2==y1) or (y-2==y1))) or ((y+1==y1 and (x+2==x1) or (x-2==x1)) or (y-1==y1 and (x+2==x1) or (x-2==x1)))
print("ot [",x,y,"] kordinatadan [",x1,y1,"] kordinataga  o'ta oladi : ",shart)

