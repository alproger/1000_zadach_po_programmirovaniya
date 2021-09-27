
n = int(input('Вводите целое число N (> 0) : '))
factorial  = 1

for i in range(1, n+1) :
    factorial *= i  

print(f'{n}! = ',factorial)

