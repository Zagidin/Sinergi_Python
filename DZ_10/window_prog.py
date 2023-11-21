# Импортиируем tkinter и библиотеку для рандомных выводов значений
from tkinter import *
import random

# Данный словарь по условию
definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}


# Создаём функцию с рандомным выводом и удалением
def show_random_definition():
    random_keys = random.choice(list(definitions.keys())) # Выводим рандомное значение, не определение
    text_polzovatel.delete('0.0', END) # Очистка
    text_polzovatel.insert('0.0', definitions[random_keys]) # 
    


# Создаём главное окно 
root = Tk()
root.title("Определения Python") # Задаём заголовок для окна
root.geometry("400x300") # Задаём размеры для окна

# Создаём поле для ввода
# entry = Entry(root, height=10)
text_polzovatel = Text(root, height=3, width=50)
text_polzovatel.pack(pady=30)

# Создаём кнопку для "Показать определение"
bt1 = Button(root, text="Показать определение", command=show_random_definition)
bt1.pack(pady=3) # Запускаем кнопку

# Запускаем окно
root.mainloop()