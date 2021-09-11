vq = int(input(" Скорость лодки : "))
vo = int(input("скорость течения реки  : "))
to = 1
tq = 2
s = (vq + vo)*to + (vq-vo)*tq
print("путь S, пройденный лодкой : ",s)
