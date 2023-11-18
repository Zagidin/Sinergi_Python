# cycles2 = int(input('Введите любое число: '))

# [print(i, end=' | ') if cycles2 != i  else print(i, end=' | \n') for i in range(0, cycles2 + [1 if cycles2 > 0 else -1][0], [1 if cycles2 > 0 else -1][0])]





# # Сохраняем этаж
# def Floor(stop_floor):
#     for i in range(stop_floor+1):
#         print(i+1, end='\n' * 2 + '\n_')
#     print(f'{stop_floor} Этаж')


# # def Floor_down(stop_floor):
# #     for i in range(contenner, ):
        
# floor = int(input('Введите этаж: '))

# if floor == 10:
#     Floor(floor)
# elif floor == 9:
#     Floor(floor)
# elif floor == 8:
#     Floor(floor)
# elif floor == 7:
#     Floor(floor)
# elif floor == 6:
#     Floor(floor)
# elif floor == 5:
#     Floor(floor)
# elif floor == 4:
#     Floor(floor)
# elif floor == 3:
#     Floor(floor)
# elif floor == 2:
#     Floor(floor)
# elif floor == 1:
#     print('Первый этаж')

# spisok = [1, 2, 3, 4, 5, 6]
# print(spisok)
# print("Длина списка:", len(spisok))

# spisok.append(9) # метод для добавления в список
# print(spisok)
# print("Длина второго списка:", len(spisok))

# a = list() # Вывод: []
# a.append('Zagidin')
# a.append(16)
# a.append('age')
# print(a)

spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(f'{spisok}\n{spisok[0].append(list())}\n{spisok[0][3].append(0)}\n{spisok}')
