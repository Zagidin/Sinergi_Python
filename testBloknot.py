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

# spisok = [
#     [1, 1, 4],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
# print(f'{spisok}\n{spisok[0].append(list())}\n{spisok[0][3].append(0)}\n{spisok}')

# res1 = spisok[0][0]
# res2 = spisok[0][1]
# print(res1 + res2)

# spisok = [
#     1, 2, 3, 5
# ]

# spisok.insert(3, 4)
# print(spisok)

# a = [1, 0, 3, 0]
# a.append(5)
# print(*a)
# print(*a, sep='/')
# a.pop()
# print(*a)
# a.reverse()
# print(*a)

# n = int(input('Введите количество значений в списке: '))

# spisok = [True, 'da']
# # contenner = 0
# # 
# # for i in range(n):
#     # spisok_znachenie = int(input('Введите значения списка: '))
#     # spisok.append(spisok_znachenie)
#     # contenner += spisok_znachenie
#     # 
# print("Ваш список:", *spisok)
# # print(contenner)

# print([list(map(int, input().split('\n'))) for _ in range(4)])
# print([list(map(int, input().split('\n'))) for _ in range(4)])


# ------------------------------------КУРС по Stepik -------------------------------------------------------------------

# n = int(input())
# contenner = 1

# for i in range(1, n+1):
#     contenner *= i

# print(contenner)
# ------------------------------------------------------------
# print(__import__('math').factorial(int(input())))

# numbers = [int(input()) for _ in range(10)]

# composition = 1
# for num in numbers:
#     if num != 0:
#         composition *= num

# print(composition)
# -----------------------------------------------------------------

# n = int(input())

# counter = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         counter += i
        
# print(counter)
# ---------------------------------------------------------------------

# n = int(input())

# counter = 0
# for i in range(1, n):
#     res = ((-1)**(i + 1 )) * i
#     print(res)

# -------------------Знака чередование---------------------------

# n = int(input())

# counter = 0
# for i in range(n):
#     if i % 2 == 0:
#         counter += i + 1
#     else:
#         counter -= i + 1
    
# print(counter)

# ---------------------------------------------------------
n = int(input())

counter = ''
for i in range(n):
    n = input()
    counter += n + ' '

spisok1 = counter.split(' ') # ['1', '2', '3', '']

spisok1.pop() # ['1', '2', '3']

spisok_num = list(map(int, spisok1)) # [1, 2, 3]
print(max(spisok_num))
spisok_num.remove(max(spisok_num)) # [1, 2]
print(max(spisok_num))
