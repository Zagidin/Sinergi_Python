cycles2 = int(input('Введите любое число: '))

# Если число положительное 
if cycles2 > 0:
    contener = -1
    while contener < cycles2:
        contener += 1
        print(contener, end=' | ')
        
# Если число отрицательное 
elif cycles2 < 0:
    contener = 1
    while contener > cycles2:
        contener -= 1
        print(contener, end=' | ')

# Это чтоб перейти на новую строку.
print()
