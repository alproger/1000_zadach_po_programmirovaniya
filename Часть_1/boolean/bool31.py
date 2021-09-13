a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
print(a,b,c,"tomonli 3burchak teng yonli : ",(a==b  and b!=c)or(a==c and a==b)or(b==c and b!=a))