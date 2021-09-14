print("Вводите целое число, лежащее в диапазоне 1–999 ")
num = int(input("число : "))

if num % 2 == 0 :
    print('четное ', end='')
    if num < 10 and num > 0 :
        print('однозначное число')
    
    elif num > 9 and num < 100 :
        print('двузначное число')
    
    elif num > 99 and num < 1000 :
        print('трехзначное число')

else:
    print('нечетное ', end='')
    if num < 10 and num > 0 :
        print('однозначное число')
    
    elif num > 9 and num < 100 :
        print('двузначное число')
    
    elif num > 99 and num < 1000 :
        print('трехзначное число')

