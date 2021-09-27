n = int(input('Вводите целое число N (> 0) : '))
pro = 1

for i in range(1,n+1) :
    pro *= i/10 


print(pro)