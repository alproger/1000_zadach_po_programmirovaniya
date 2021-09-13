print("shaxmat doskasidai kordinatani kiriting \n farzin kordinatasi : ")
x = int(input("x : "))
y = int(input("y : "))
print("farzin o'tishi kerak bo'lgan kordinata : ")
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
print("farzin [",x,y,"] kordinatadan [",x1,y1,"] kordinataga  o'ta oladi : ",(x-x1==y-y1)or((x==x1 and y!=y1) or (x!=x1 and y==y1)))

