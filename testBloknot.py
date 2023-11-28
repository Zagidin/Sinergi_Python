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
# n = int(input())

# counter = ''
# for i in range(n):
#     n = input()
#     counter += n + ' '

# spisok1 = counter.split(' ') # ['1', '2', '3', '']

# spisok1.pop() # ['1', '2', '3']

# spisok_num = list(map(int, spisok1)) # [1, 2, 3]
# print(max(spisok_num))
# spisok_num.remove(max(spisok_num)) # [1, 2]
# print(max(spisok_num))

# from math import * 

# n = int(input())

# counter = 1
# for i in range(1, n+1):
#     Xn = i + counter

# print(int(counter))

# set1, set2 = [1, 2, 3, 5], [2, 5, 1, 4]

# intersection_set = set(set1) & set(set2)
# print(intersection_set)

# -----------------------------------Банк создание или пополнение------------------------------------------------
# while True:
#     bank = dict()

#     n = int(input("Сколько запросов пришло Банку? 2 для создания и внесения!: "))

#     for i in range(n):
#         req = input("Введите запрос < create / add > : ")
        
#         if req == 'create':
#             k = input("Введите название нового ключа: ")
#             bank[k] = 0
#             print('Успешно создано!')
            
#         if req == 'add':
#             k = input("Введите ключ ячейки для пополнения, если вы его создали недвано, то созданную недавно: ")
#             summa = int(input("Сумма для пополнения --> "))
            
#             if k not in bank.keys():
#                 print("Извините, такой ячейки нет!")
#             else:
#                 bank[k] += summa
#         else:
#             print("Извините, что-то пошло не так, попробуйте обновить!")

#     polzovatel = input("Ваша роль? ")

#     if polzovatel == 'Zagidin':
#         print(f'Сегодня добавились: {bank}')
#     else:
#         print("Спсасибо за доверие)")
        
#----------------------------------------------------------------------------------------------------------------------

# from tkinter import *


# def no_bt2(event):
#     run = 15
#     new_x = event.x + run
#     new_y = event.y + new_x
#     bt2.place(y=new_x, x=new_y)


# def Otvet():
#     new_window = Toplevel()
#     new_window.title("РКСИ")
#     new_window.geometry("200x50")
#     text_new_window = Label(new_window, text="Мы не сомнивались!\nСиди дома и отдыхай)", pady=10)
#     text_new_window.pack()


# root = Tk()
# root.geometry("165x135")

# root.title("ОПРОС")

# text = Label(root, text="Пойти на 1 пару?", pady=20)
# text.pack()

# bt1 = Button(root, text="ДА", font=("bold", 10), padx=10, pady=5, command=Otvet)
# bt1.pack()

# bt2 = Button(root, text="НЕТ", font=("bold", 10), padx=10, pady=5)
# bt2.bind("<Motion>", no_bt2)
# bt2.pack()

# root.mainloop()

# ----------------------------------------------------------------------------------------------------

# n = int(input())

# F1 = 1
# F2 = 0

# for i in range(n):
#     F3 = F1
#     F1 += F2
#     F2 = F3
#     print(F2, end=" ")
# -------------------------------------------------------------------------------------

# i = 0

# while i < 10:
#     print('Zagidin')
#     i += 1
# --------------------------------------------------------------

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# i = 0
# while i < 101:
#     print(i)
#     i += 1

# text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()

# print('Сумма чисел равна', total)

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(12 + 9)

# text = input()

# counter = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     counter += 1
#     text = input()
    
# print(counter)

# number = int(input())

# counter = ''
# while number % 7 == 0:
#     if number % 7 == 0:
#         counter += str(number) + '\n'
#     else:
#         break
#     number = int(input())

# print(counter)

# number = int(input())

# counter = 0
# while number >= 0:
#     counter += number
#     number = int(input())
    
# print(counter)

# number = int(input())

# counter = 0

# while number > 0 and number <= 5:
#     if number == 5:
#         counter += 1
#     number = int(input())

# print(counter)

# n = int(input())

# counter = 0
# while n >= 25:
#     counter += 1
#     n = n - 25

# while n >= 10:
#     counter += 1
#     n = n - 10

# while n >= 5:
#     counter += 1
#     n = n - 5

# while n >= 1:
#     counter += 1
#     n = n - 1
    
# print(counter)

# num = int(input())

# my_number_counter = ''

# while num != 0:
#     num_end = num % 10
#     my_number_counter += str(num_end) + ' '
#     num = num // 10
    
# my_number_counter = my_number_counter.split(' ')
# my_number_counter.pop()
# my_number_counter = list(map(int, my_number_counter))

# print(f'Максимальное цифра равна {max(*my_number_counter)}\nМинимальная цифра равна {min(*my_number_counter)}')

#----------------------------------------------------------------------------------------------------------------------------------

# number = int(input())
# number2 = number

# # В список для длины
# counter_len = ''
# while number2 != 0:
#     end_num = number2 % 10
#     counter_len += str(end_num) + ' '
#     number2 = number2 // 10

# # Для выведения одного числа 5-й пункт
# counter_one_end = int(counter_len.replace(' ', ''))
# counter_one_num = counter_one_end

# # Деление числа по пробелам и переприсваивание переменной длиной
# counter_len = counter_len.split(' ')
# counter_len.pop()
# counter_len = len(counter_len)

# # Находим сумму чисел и умножение
# counter_summa = 0
# counter_myltiply = 1
# while number != 0:
#     end_num = number % 10
#     counter_summa += end_num
#     counter_myltiply *= end_num
#     number = number // 10

# # Получаю первоначальное число
# counter_one_end_summ = ''
# while counter_one_end != 0:
#     end_num = counter_one_end % 10
#     counter_one_end_summ += str(end_num) + ' '
#     counter_one_end = counter_one_end // 10

# # Сумма первого и последнего числа
# counter_one_end_summ = counter_one_end_summ.split(' ')
# counter_one_end_summ.pop()
# counter_one_end_summ = list(map(int, counter_one_end_summ))
# counter_one_end_summ = counter_one_end_summ[0] + counter_one_end_summ[-1]

# # Среднее арифметическая сумма и делить на количество чисел 
# counter_average_value = counter_summa / counter_len

# # Вывод первой цифры в числе 5-й пункт
# counter_one_num = counter_one_num % 10

# print(f'{counter_summa}\n{counter_len}\n{counter_myltiply}\n{counter_average_value}\n{counter_one_num}\n{counter_one_end_summ}')

#---------------------------------------------------------------------------------------------------------------------------------------------

# number = int(input())
# num = number
# try:
    
#     counter_end_num = ''
#     while number != 0:
#         end_num = number % 10
#         counter_end_num += str(end_num) + ' '
#         number = number // 10

#     counter_one_end_num = int(counter_end_num.replace(' ', ''))
#     counter_end_num = counter_end_num.split(' ')
#     counter_end_num.pop()
#     counter_end_num = list(map(int, counter_end_num))

#     counter_one_num = ''
#     while counter_one_end_num != 0:
#         end_num = counter_one_end_num % 10
#         counter_one_num += str(end_num) + ' '
#         counter_one_end_num = counter_one_end_num // 10
            
#     counter_one_num = counter_one_num.split(' ')
#     counter_one_num.pop()
#     counter_one_num = list(map(int, counter_one_num))

#     counter_one_num = int(counter_one_num[1])
#     print(counter_one_num)
# except IndexError:
#     res = num % 10
#     if num == 0:
#         print(0)
#     else:
#         print(0)
# -----------------------------------------------------------------------------

# number = int(input())
# print(str(number)[1])

#------------------------------------------------------------------------------------------------

# print('YES' if len(set(input())) == 1 else 'NO')

#---------------------------------------------------------------------------------------------------------

number = int(input())

counter = ''
while number != 0:
    end_num = number % 10
    counter += str(end_num) + ' '
    number = number // 10
    
counter_num = int(counter.replace(' ', ''))

counter = counter.split(' ')
counter.pop()
counter = list(map(int, counter))



if counter[-1] < counter[-2] and counter[-1] < counter[-3] and counter[-2] < counter[-3]:
    print('YES')
else:
    print('NO')