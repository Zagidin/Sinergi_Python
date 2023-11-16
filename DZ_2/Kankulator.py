print("Привет! Это простой канкулятор.\nДоступные операции: + ; -")
operation, num1, num2 = input('Введите операцию: '), float(input('Введите первое число: ')), float(input('Введите второе число: '))

if operation == '+':
    print('Ваш результат:', num1 + num2)
elif operation == '-':
    print('Ваш результат:', num1 - num2)
