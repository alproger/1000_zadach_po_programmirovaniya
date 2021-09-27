a = int(input('Вводите вещественное число A (> 0) : '))
n = int(input('Вводите целое число N (> 0) : '))


kvA = 1
for i in range(n) :
    kvA *= a

print(kvA)