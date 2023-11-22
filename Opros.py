from tkinter import *


def no_bt2(event):
    run = 15
    new_x = event.x + run
    new_y = event.y + new_x
    bt2.place(y=new_x, x=new_y)


def Otvet():
    new_window = Toplevel()
    new_window.title("РКСИ")
    new_window.geometry("200x50")
    text_new_window = Label(new_window, text="Мы не сомнивались!\nСиди дома и отдыхай)", pady=10)
    text_new_window.pack()


root = Tk()
root.geometry("165x135")

root.title("ОПРОС")

text = Label(root, text="Пойти на 1 пару?", pady=20)
text.pack()

bt1 = Button(root, text="ДА", font=("bold", 10), padx=10, pady=5, command=Otvet)
bt1.pack()

bt2 = Button(root, text="НЕТ", font=("bold", 10), padx=10, pady=5)
bt2.bind("<Motion>", no_bt2)
bt2.pack()

root.mainloop()