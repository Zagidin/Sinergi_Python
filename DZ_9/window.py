# Импортируем библиотеку
from tkinter import *


# Создаём функцию, которая будет выводится в консоле при нажатии кнопки
def hello(event):
    print("Привет, Загидин!")


# Создаём фунцию, которая будет выводить введённый тект пользователем в новом окне
def pokazat_text():
    text = entry.get()
    new_window = Toplevel(root)
    new_window.geometry("300x100") # Задаю размеры для второго окна
    label = Label(new_window, text=text)
    label.pack() 

# Создаём функцию, которая будет очищать поле ввода 
def clear_inputText():
    entry.delete(0, END)


# Создаём главное окно
root = Tk()

root.geometry("400x200") # Задаём размеры окну

# Создаём поле для ввода в нашем созданном окне
entry = Entry(root)
entry.pack() # Выводим это созданное поле для ввода 

# Создаём кнопку в нашем созданном окне
bt1 = Button(root)
# Присваеваем к кнопке функцию hello
bt1.bind("<Button-1>", hello) # Кнопка ПКМ
bt1.bind("<Button-2>", hello) # Кнопка Колесо
bt1.bind("<Button-3>", hello) # Кнопка ЛКМ  
bt1.pack() # Выводим кнопку в окне

# Создаём кнопку / Показать / Активируем функцию спомощью command
bt2 = Button(root, text="Показать", command=pokazat_text)
bt2.pack()

# Создаём кнопку для очищения поля для ввода текта / присвоили функцию удаления 
bt3 = Button(root, text="Очистить", command=clear_inputText)
bt3.pack()

# Цикл обработки исключений 
root.mainloop()
