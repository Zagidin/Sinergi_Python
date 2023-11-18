cycles1 = int(input('Введите любое число: '))

# Если пользователь введёт положительное значение
if cycles1 > 0:
    for i in range(cycles1+1):
        print(i, end=' | ')
        
# Если пользователь введёт отрицательное значение
else:
    for i in range(0, cycles1-1, -1):
        print(i, end=' | ')

# Это чтоб перейти на новую строку
print()