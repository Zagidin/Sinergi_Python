spisok_1 = ['Zaga', 16, True, 2007, 'Dagestan', 2000, 'Дербент', 17.08, 'Белиджи', False]

# Выводим список полностью и 5 элеметов и 3 конечные элементы
print(f'{spisok_1}\n{spisok_1[0:5]}\n{spisok_1[-3::]}')

# Выводим каждый второй элемент списка
result = spisok_1[1::2]
print(result)

# Замена третьего элемента списка
spisok_1[2] = False
print(spisok_1)
