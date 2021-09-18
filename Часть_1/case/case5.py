print('Введите вещественные числа A и B (В не равно 0)')
a = float(input('A : '))
b = float(input('B : '))

operation =  input('Вводите операции (+, -, *, /) : ')

def switch(num1,num2,operation):
    
    operations = ['+', '-', '*', '/']

    if operation in operations:
        
        if operation == '+' :
            return num1 + num2

        elif operation == '-' :
            return num1 - num2

        elif operation == '*' :
            return num1 * num2
        
        elif operation == '/' :
            return num1 / num2
            
    else:
        print('error') 

print(switch(1,2,'+'))
