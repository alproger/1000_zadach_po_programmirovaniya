abcd = int(input("Вводите четырехзначное число : "))
cheking = abcd//1000 == abcd%10 and abcd//100%10 == abcd%100//10
print("Данное число читается одинаково слева направо и справа налево : ",cheking)


