a = int(input("a : "))
b = int(input("b : "))
print(f"Ровно одно из чисел {a} и {b} нечетное : ",(a%2!=0 and b%2==0)or(a%2==0 and b%2!=0))


