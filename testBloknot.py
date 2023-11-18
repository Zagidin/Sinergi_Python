cycles2 = int(input('Введите любое число: '))

[print(i, end=' | ') if cycles2 != i  else print(i, end=' | \n') for i in range(0, cycles2 + [1 if cycles2 > 0 else -1][0], [1 if cycles2 > 0 else -1][0])]





# Сохраняем этаж
def Floor(stop_floor):
    for i in range(stop_floor+1):
        print(i+1, end='\n' * 2 + '\n_')
    print(f'{stop_floor} Этаж')


# def Floor_down(stop_floor):
#     for i in range(contenner, ):
        
floor = int(input('Введите этаж: '))

if floor == 10:
    Floor(floor)
elif floor == 9:
    Floor(floor)
elif floor == 8:
    Floor(floor)
elif floor == 7:
    Floor(floor)
elif floor == 6:
    Floor(floor)
elif floor == 5:
    Floor(floor)
elif floor == 4:
    Floor(floor)
elif floor == 3:
    Floor(floor)
elif floor == 2:
    Floor(floor)
elif floor == 1:
    print('Первый этаж')