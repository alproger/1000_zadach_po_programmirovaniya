print("Вводите год ")
yil = int(input("год : "))
if yil%4 == 0 and yil%100 != 0 :
    print(f'в {yil} году есть 366 дней ')
elif (yil%100 == 0 and yil%400 == 0 ):
    print(f'в {yil} году есть 366 дней ')
else:
    print(f'в {yil} году есть 365 дней ')
