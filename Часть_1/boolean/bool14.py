a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
print(f"Ровно одно из чисел {a}, {b}, {c} положительное: ",(a>0 and b<=0 and c<=0)or(a<=0 and b>0 and c<=0)or(a<=0 and b<=0 and c>0))


