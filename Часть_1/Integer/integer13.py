xyz = int(input("Вводите трехзначное число : "))
print("В нем зачеркнули первую слева цифру иприписали ее справа :  ",xyz//100+100*(xyz%100//10)+10*(xyz%10))



